from app.providers.mock_provider import MockProvider

provider = MockProvider()

jobs = provider.search()

print(f"Found {len(jobs)} jobs\n")

for job in jobs:
    print(job.company)
    print(job.title)
    print(job.location)
    print()