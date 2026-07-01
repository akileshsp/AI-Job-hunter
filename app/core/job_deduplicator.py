class JobDeduplicator:

    def remove_duplicates(self, jobs):

        unique = {}

        for job in jobs:

            key = (
                job.title.strip().lower(),
                job.company.strip().lower(),
                job.location.strip().lower()
            )

            if key not in unique:
                unique[key] = job

        print(f"🧹 Removed {len(jobs) - len(unique)} duplicate jobs")

        return list(unique.values())