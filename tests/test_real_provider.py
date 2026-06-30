from app.providers.real_job_provider import RealJobProvider

provider = RealJobProvider()

jobs = provider.search()

print(f"\nFound {len(jobs)} jobs\n")

for job in jobs:
    print("--------------------------------")
    print(job.company)
    print(job.title)
    print(job.location)