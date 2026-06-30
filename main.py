import json
from pathlib import Path

from app.search.mock_search import MockSearch

APP_NAME = "AI Job Hunter"
VERSION = "1.0.0"


def load_settings():
    config_path = Path("config/settings.json")

    if not config_path.exists():
        print("❌ settings.json not found")
        return None

    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    print("=" * 50)
    print(f"🚀 {APP_NAME} v{VERSION}")
    print("=" * 50)

    settings = load_settings()

    if settings:
        print("✅ Configuration Loaded Successfully")
        print(f"👤 User      : {settings['user']['name']}")
        print(f"📍 Location  : {settings['user']['location']}")
        print(f"💰 Salary    : {settings['user']['expected_ctc']}")
        print(f"💼 Experience: {settings['user']['experience']} Years")

    print("\n🎯 AI Job Hunter is Ready!")

    print("\n🔍 Searching Jobs...\n")

    search = MockSearch()
    jobs = search.search()

    print(f"Found {len(jobs)} Jobs\n")

    for job in jobs:
        print("--------------------------------")
        print(f"Company : {job.company}")
        print(f"Role    : {job.title}")
        print(f"Location: {job.location}")
        print(f"Source  : {job.source}")
        print(f"URL     : {job.url}")


if __name__ == "__main__":
    main()