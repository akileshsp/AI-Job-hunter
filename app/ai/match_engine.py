from app.ai.profile_extractor import ProfileExtractor
from app.ai.profile_builder import ProfileBuilder
from app.ai.resume_parser import ResumeParser


class MatchEngine:

    def __init__(self):

        parser = ResumeParser()
        extractor = ProfileExtractor()
        builder = ProfileBuilder()

        resume_text = parser.parse("resume/resume.pdf")

        raw_profile = extractor.extract(resume_text)

        self.profile = builder.build(raw_profile)

    def calculate_score(self, job):

        score = 0.0

        matched = []

        content = f"{job.title} {job.description}".lower()

        # -----------------------------
        # Skill Match (60)
        # -----------------------------
        skills = self.profile.get("skills", [])

        if skills:

            per_skill = 60 / len(skills)

            for skill in skills:

                if skill.lower() in content:

                    matched.append(skill)

                    score += per_skill

        # -----------------------------
        # Tool Match (20)
        # -----------------------------
        tools = self.profile.get("tools", [])

        if tools:

            per_tool = 20 / len(tools)

            for tool in tools:

                if tool.lower() in content:

                    score += per_tool

        # -----------------------------
        # Job Title Match (10)
        # -----------------------------
        for title in self.profile.get("job_titles", []):

            if title.lower() in job.title.lower():

                score += 10

                break

        # -----------------------------
        # Experience (5)
        # -----------------------------
        if self.profile.get("experience", 0) >= 5:

            score += 5

        # -----------------------------
        # Remote Bonus (5)
        # -----------------------------
        if "remote" in job.location.lower():

            score += 5

        job.match_score = round(min(score, 100), 2)

        job.matched_skills = matched

        if job.match_score >= 90:
            job.recommendation = "★★★★★ Excellent Match"
        elif job.match_score >= 75:
            job.recommendation = "★★★★☆ Very Good Match"
        elif job.match_score >= 60:
            job.recommendation = "★★★☆☆ Good Match"
        elif job.match_score >= 40:
            job.recommendation = "★★☆☆☆ Fair Match"
        else:
            job.recommendation = "★☆☆☆☆ Weak Match"

        return job.match_score