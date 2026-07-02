class JobRanker:

    def rank(self, jobs):

        def score(job):

            total = getattr(job, "match_score", 0)

            title = (job.title or "").lower()
            location = (job.location or "").lower()
            description = (job.description or "").lower()

            searchable = f"{title} {description}"

            # Seniority
            if "senior" in title:
                total += 15

            if "lead" in title:
                total += 15

            if "principal" in title:
                total += 15

            if "manager" in title:
                total += 10

            # Domain relevance
            keywords = {
                "packaging": 25,
                "label": 20,
                "labeling": 20,
                "artwork": 20,
                "prepress": 20,
                "print": 15,
                "quality": 15,
                "regulatory": 15,
                "pharma": 15,
                "medical": 10,
                "engineer": 10,
                "designer": 10,
                "specialist": 10
            }

            for word, points in keywords.items():

                if word in searchable:
                    total += points

            # Location priority
            if "bengaluru" in location or "bangalore" in location:
                total += 30

            elif "india" in location:
                total += 20

            elif "remote" in location:
                total += 15

            elif "hybrid" in location:
                total += 10

            return total

        ranked = sorted(
            jobs,
            key=score,
            reverse=True
        )

        print(f"⭐ Ranked {len(ranked)} jobs")

        return ranked