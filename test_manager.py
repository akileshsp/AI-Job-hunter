from app.providers.provider_manager import ProviderManager

manager = ProviderManager()

jobs = manager.search_jobs()

print("=" * 50)
print("🚀 Provider Manager")
print("=" * 50)

print(f"\nFound {len(jobs)} jobs\n")

for job in jobs:
    print("--------------------------------")
    print(f"Company : {job.company}")
    print(f"Role    : {job.title}")
    print(f"Location: {job.location}")
    print(f"Source  : {job.source}")