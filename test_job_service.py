from app.services.job_service import JobService

service = JobService()

jobs = service.run()

print("\n========== FINAL JOBS ==========\n")

for job in jobs:

    print("--------------------------------")
    print("Company :", job.company)
    print("Role    :", job.title)
    print("Location:", job.location)
    print("Score   :", job.match_score)