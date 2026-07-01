from difflib import SequenceMatcher


class JobMatcher:

    def similarity(self, a, b):

        return SequenceMatcher(
            None,
            a.lower(),
            b.lower()
        ).ratio()

    def match(self, profile, job):

        score = 0

        matched = []
        missing = []

        searchable = " ".join([

            job.title or "",

            job.description or "",

            job.company or "",

            job.location or "",

            job.department or ""

        ]).lower()

        # Job Titles (Highest Weight)

        for role in profile.get("job_titles", []):

            role = role.strip()

            if not role:
                continue

            if role.lower() in searchable:

                score += 35

                matched.append(role)

            elif self.similarity(role, job.title) > 0.70:

                score += 25

                matched.append(role)

        # Skills

        for skill in profile.get("skills", []):

            skill = skill.strip()

            if not skill:
                continue

            if skill.lower() in searchable:

                score += 10

                matched.append(skill)

            else:

                missing.append(skill)

        # Tools

        for tool in profile.get("tools", []):

            tool = tool.strip()

            if not tool:
                continue

            if tool.lower() in searchable:

                score += 8

                matched.append(tool)

        # Industry

        for industry in profile.get("industries", []):

            if industry.lower() in searchable:

                score += 12

                matched.append(industry)

        # Experience Bonus

        exp = profile.get("experience", 0)

        if exp >= 10:

            score += 10

        elif exp >= 5:

            score += 5

        matched = sorted(set(matched))
        missing = sorted(set(missing))

        score = min(score, 100)

        job.match_score = score
        job.matched_skills = matched
        job.missing_skills = missing

        if score >= 90:
            job.recommendation = "🔥 Excellent Match"
        elif score >= 75:
            job.recommendation = "✅ Strong Match"
        elif score >= 55:
            job.recommendation = "👍 Good Match"
        elif score >= 35:
            job.recommendation = "⚠ Possible Match"
        else:
            job.recommendation = "❌ Low Match"

        return job