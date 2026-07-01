import json

from app.database.database import initialize_database
from app.services.job_service import JobService


def load_config():
    with open("config/settings.json", "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    config = load_config()
    user = config["user"]

    print("=" * 60)
    print("🚀 AI JOB HUNTER v1.0")
    print("=" * 60)

    print(f"👤 User         : {user['name']}")
    print(f"📧 Email        : {user['email']}")
    print(f"📍 Location     : {user['location']}")
    print(f"💰 Expected CTC : {user['expected_ctc']}")
    print(f"💼 Experience   : {user['experience']} Years")

    # Initialize database
    initialize_database()

    # Run Job Search
    service = JobService()
    jobs = service.run()

    print("\n" + "=" * 60)
    print("📈 FINAL SUMMARY")
    print("=" * 60)

    print(f"Jobs Processed : {len(jobs)}")

    excellent = len([j for j in jobs if j.match_score >= 90])
    good = len([j for j in jobs if 75 <= j.match_score < 90])
    average = len([j for j in jobs if j.match_score < 75])

    print(f"★★★★★ Excellent : {excellent}")
    print(f"★★★★☆ Good      : {good}")
    print(f"★★★☆☆ Average   : {average}")

    if jobs:

        best = jobs[0]

        print("\n🥇 BEST MATCH")
        print(f"Company        : {best.company}")
        print(f"Role           : {best.title}")
        print(f"Location       : {best.location}")
        print(f"AI Score       : {best.match_score}%")
        print(f"Recommendation : {getattr(best, 'recommendation', '')}")
        print(f"Source         : {best.source}")

    print("\n🎉 AI Job Hunter Backend v1.0 Ready")


if __name__ == "__main__":
    main()