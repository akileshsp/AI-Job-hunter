import requests


class JobAPI:

    def get_json(self, url, headers=None):

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=15
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:
            print(f"API Error: {e}")
            return None