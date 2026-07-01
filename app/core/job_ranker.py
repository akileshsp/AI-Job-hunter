class JobRanker:

    def rank(self, jobs):

        def score(job):

            score = 0

            if hasattr(job, "match_score"):
                score += job.match_score

            if "Packaging" in job.title:
                score += 20

            if "Label" in job.title:
                score += 15

            if "Artwork" in job.title:
                score += 15

            if "Remote" in job.location:
                score += 5

            return score

        jobs.sort(
            key=score,
            reverse=True
        )

        print(f"⭐ Ranked {len(jobs)} jobs")

        return jobs