import re


class ResumeOptimizer:

    def optimize(self, profile, job):

        title = (job.title or "").lower()
        description = (job.description or "").lower()

        searchable = f"{title} {description}"

        matched = []
        missing = []

        # Match skills
        for skill in profile.get("skills", []):

            if skill.lower() in searchable:
                matched.append(skill)
            else:
                missing.append(skill)

        # Match tools
        for tool in profile.get("tools", []):

            if tool.lower() in searchable and tool not in matched:
                matched.append(tool)

        total = len(profile.get("skills", []))

        if total == 0:
            ats_score = 0
        else:
            ats_score = round(
                (len(matched) / total) * 100,
                2
            )

        suggestions = []

        for skill in missing[:10]:

            suggestions.append(
                f"Consider adding experience related to '{skill}' if it accurately reflects your background."
            )

        return {

            "ats_score": ats_score,

            "matched_skills": matched,

            "missing_skills": missing,

            "suggestions": suggestions

        }