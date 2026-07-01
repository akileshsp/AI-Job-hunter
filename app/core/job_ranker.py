class JobRanker:

    def rank(self, jobs):

        def score(job):

            total = getattr(job, "match_score", 0)

            title = (job.title or "").lower()
            location = (job.location or "").lower()

            # Senior roles
            if "senior" in title:
                total += 15

            if "lead" in title:
                total += 15

            if "principal" in title:
                total += 15

            if "manager" in title:
                total += 10

            # Remote bonus
            if "remote" in location:
                total += 5

            # Hybrid bonus
            if "hybrid" in location:
                total += 3

            return total

        ranked = sorted(
            jobs,
            key=score,
            reverse=True
        )

        print(f"⭐ Ranked {len(ranked)} jobs")

        return ranked