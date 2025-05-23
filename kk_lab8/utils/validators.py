def validate_product_fields(record: dict, reference: dict) -> None:
	issues = []
	for field, expected_val in reference.items():
		if field in ('id', 'alias'):
			continue
		actual_val = record.get(field)
		if str(actual_val) != str(expected_val):
			issues.append(
				f"Поле '{field}': получили '{actual_val}', ожидали '{expected_val}'"
			)
	assert not issues, "\n".join(issues)
