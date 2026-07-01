class JobMatcher:

    def match(self, profile, job):

        score = 0

        matched = []
        missing = []

        title = (job.title or "").lower()
        description = (job.description or "").lower()

        searchable = f"{title} {description}"

        # Job Titles (highest weight)
        for role in profile.get("job_titles", []):

            if role.lower() in searchable:

                score += 35

                matched.append(role)

        # Skills
        for skill in profile.get("skills", []):

            if skill.lower() in searchable:

                score += 10

                matched.append(skill)

            else:

                missing.append(skill)

        # Tools
        for tool in profile.get("tools", []):

            if tool.lower() in searchable:

                score += 8

                matched.append(tool)

        # Experience
        experience = profile.get("experience", 0)

        if experience >= 10:
            score += 10
        elif experience >= 5:
            score += 5

        # Remove duplicates
        matched = list(dict.fromkeys(matched))
        missing = list(dict.fromkeys(missing))

        score = min(score, 100)

        job.match_score = score
        job.matched_skills = matched
        job.missing_skills = missing

        if score >= 85:
            job.recommendation = "🔥 Excellent Match"
        elif score >= 70:
            job.recommendation = "✅ Strong Match"
        elif score >= 50:
            job.recommendation = "👍 Good Match"
        elif score >= 30:
            job.recommendation = "⚠ Partial Match"
        else:
            job.recommendation = "❌ Low Match"

        return job