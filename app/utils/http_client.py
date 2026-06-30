import requests


class HttpClient:

    @staticmethod
    def get(url):

        print(f"🌐 GET {url}")

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        return response.json()