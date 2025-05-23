import requests

BASE_URL = "http://shop.qatl.ru"

class ApiClient:
    @staticmethod
    def get_products():
        return requests.get(f"{BASE_URL}/api/products")

    @staticmethod
    def add_product(product_data):
        return requests.post(f"{BASE_URL}/api/addproduct", json=product_data)

    @staticmethod
    def edit_product(product_data):
        return requests.post(f"{BASE_URL}/api/editproduct", json=product_data)

    @staticmethod
    def delete_product(product_id):
        return requests.get(f"{BASE_URL}/api/deleteproduct", params={"id": product_id})
