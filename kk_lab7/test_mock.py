import requests
import json


class ExchangeService:
    """
    Сервис для получения курсов валют из локального мок-сервиса.
    """
    def __init__(self, base_url: str = "http://127.0.0.1:4545", endpoint: str = "/exchange"):
        self._url = f"{base_url}{endpoint}"

    def fetch(self, currency: str) -> float:
        params = {"currency": currency}
        resp = requests.get(self._url, params=params)
        try:
            resp.raise_for_status()
        except requests.HTTPError as http_err:
            raise RuntimeError(f"HTTP error: {http_err}")

        payload = resp.json()
        if "rate" not in payload:
            raise ValueError("В ответе отсутствует параметр 'rate'.")
        return payload["rate"]


def main():
    service = ExchangeService()
    user_input = input("Введите валюту (USD или EUR): ").strip().upper()
    try:
        result = service.fetch(user_input)
        print(f"Текущий курс для {user_input} = {result}")
    except Exception as err:
        print(f"Ошибка при получении курса: {err}")


if __name__ == "__main__":
    main()