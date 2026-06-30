from app.services.job_service import JobService

service = JobService()

jobs = service.run()

print("\n========== FINAL JOBS ==========\n")

for job in jobs:

    print("=" * 60)
    print("Company        :", job.company)
    print("Role           :", job.title)
    print("Location       :", job.location)
    print("AI Score       :", f"{job.match_score}%")
    print("Recommendation :", job.recommendation)
    print("Matched Skills :")

    for skill in job.matched_skills:
        print("   ✔", skill)

    print("=" * 60)