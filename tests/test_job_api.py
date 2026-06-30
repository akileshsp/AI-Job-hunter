from app.job_sources.job_api import JobAPI

api = JobAPI()

jobs = api.search(
    "Packaging Specialist",
    "Bengaluru"
)

print("\nReturned Jobs:")
print(jobs)