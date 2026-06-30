import json
from pathlib import Path

from app.database.database import initialize_database
from app.services.job_service import JobService

APP_NAME = "AI Job Hunter"
VERSION = "2.0.0"


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

    initialize_database()

    service = JobService()
    service.run()


if __name__ == "__main__":
    main()