class JobMatcher:

    def match(self, profile, job):

        score = 0
        matched = []
        missing = []

        title = job.title.lower()

        for skill in profile.get("skills", []):

            if skill.lower() in title:
                matched.append(skill)
                score += 10
            else:
                missing.append(skill)

        score = min(score, 100)

        job.match_score = score
        job.matched_skills = matched
        job.missing_skills = missing

        if score >= 80:
            job.recommendation = "🔥 Highly Recommended"
        elif score >= 60:
            job.recommendation = "✅ Good Match"
        elif score >= 40:
            job.recommendation = "👍 Possible Match"
        else:
            job.recommendation = "❌ Low Match"

        return job