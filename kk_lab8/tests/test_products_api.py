import pytest
import json
from utils.api_client import ApiClient
from utils.validators import validate_product_fields

# Load test payloads
with open("data/test_data.json", encoding="utf-8") as file:
	data_store = json.load(file)

valid_item   = data_store["valid_product"]
boundary_set = data_store["boundary_products"]
invalid_set  = data_store["invalid_products"]

@pytest.fixture
def id_registry():
	collected = []
	yield collected
	for _id in collected:
		ApiClient.delete_product(_id)

# Creation Tests

def test_product_creation_success(id_registry):
	payload = valid_item.copy()
	resp = ApiClient.add_product(payload)
	assert resp.status_code == 200, f"Error: {resp.text}"
	body = resp.json()
	assert body.get("id") and body.get("status") == 1

	new_id = body["id"]
	id_registry.append(new_id)

	all_products = ApiClient.get_products().json()
	found = next((e for e in all_products if str(e["id"]) == str(new_id)), None)
	assert found, "Added item not found"
	validate_product_fields(found, payload)

@pytest.mark.parametrize("entry", boundary_set, ids=lambda e: f"boundary_{e['alias']}")
def test_boundary_values(entry, id_registry):
	resp = ApiClient.add_product(entry)
	assert resp.status_code == 200, resp.text
	body = resp.json()
	assert body.get("id") and body.get("status") == 1
	id_registry.append(body["id"])

@pytest.mark.parametrize("entry", invalid_set, ids=lambda e: f"invalid_{e['alias']}")
def test_reject_invalid(entry):
	resp = ApiClient.add_product(entry)
	with pytest.raises(ValueError):
		_ = resp.json()

#Update Tests

def test_update_existing_product(id_registry):
	initial = valid_item.copy()
	pid = ApiClient.add_product(initial).json()["id"]
	id_registry.append(pid)

	modified = valid_item.copy()
	modified.update({"id": pid, "title": "Changed Name", "alias": "changed-alias", "price": valid_item["price"] + 50})
	resp = ApiClient.edit_product(modified)
	assert resp.status_code == 200, resp.text
	assert resp.json().get("status") == 1

#Deletion Tests

def test_remove_existing_entry(id_registry):
	pid = ApiClient.add_product(valid_item.copy()).json()["id"]
	id_registry.append(pid)
	resp = ApiClient.delete_product(pid)
	assert resp.status_code == 200, resp.text

	remaining = ApiClient.get_products().json()
	assert not any(str(p["id"]) == str(pid) for p in remaining)


def test_remove_nonexistent_entry():
	resp = ApiClient.delete_product(999999999)
	if resp.status_code == 200:
		body = resp.json() if resp.text else {}
		assert body.get("status") != 1
	else:
		assert resp.status_code != 200

#Field Validation Tests 

@pytest.mark.parametrize("field", ["title", "price", "category_id"], ids=lambda f: f"no_{f}")
def test_missing_required_field(field):
	data = valid_item.copy()
	data.pop(field, None)
	resp = ApiClient.add_product(data)
	with pytest.raises(ValueError):
		_ = resp.json()

@pytest.mark.parametrize("st", [-1, 2, 100])
@pytest.mark.xfail(reason="API does not validate status")
def test_unvalidated_status(st):
	data = valid_item.copy()
	data["status"] = st
	resp = ApiClient.add_product(data)
	with pytest.raises(ValueError):
		_ = resp.json()

@pytest.mark.parametrize("hv", [-5, 2, 99])
@pytest.mark.xfail(reason="API does not validate hit")
def test_unvalidated_hit(hv):
	data = valid_item.copy()
	data["hit"] = hv
	resp = ApiClient.add_product(data)
	with pytest.raises(ValueError):
		_ = resp.json()
