import requests

slugs = [
    "openai",
    "stripe",
    "notion",
    "plaid",
    "figma",
    "dropbox",
    "coinbase",
    "datadog",
    "hubspot",
    "gitlab"
]

for slug in slugs:

    print("=" * 50)

    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"

    print(url)

    try:

        response = requests.get(url, timeout=10)

        print("Status:", response.status_code)

        if response.status_code == 200:

            jobs = response.json().get("jobs", [])

            print("Jobs:", len(jobs))

        else:

            print(response.text[:200])

    except Exception as e:

        print(e)