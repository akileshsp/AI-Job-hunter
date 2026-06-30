from app.providers.mock_provider import MockProvider

provider = MockProvider()

jobs = provider.search()

print(f"Found {len(jobs)} jobs\n")

for job in jobs:
    print(f"Company : {job.company}")
    print(f"Role    : {job.title}")
    print(f"Location: {job.location}")
    print()