from app.ai.profile_extractor import ProfileExtractor
from app.ai.resume_parser import ResumeParser


class MatchEngine:

    def __init__(self):
        parser = ResumeParser()
        extractor = ProfileExtractor()

        resume_text = parser.parse("resume/resume.pdf")
        self.profile = extractor.extract(resume_text)

    def calculate_score(self, job):

        score = 0
        matched_skills = []

        # Search in both Job Title and Description
        content = (job.title + " " + job.description).lower()

        # ---------------------------------
        # Job Title Bonus (Max 40)
        # ---------------------------------
        title = job.title.lower()

        if "packaging" in title:
            score += 20

        if "artwork" in title:
            score += 20

        # ---------------------------------
        # Skill Matching (Max 30)
        # ---------------------------------
        skill_score = 0

        for skill in self.profile["skills"]:

            if skill.lower() in content:

                if skill not in matched_skills:
                    matched_skills.append(skill)

                if skill_score < 30:
                    skill_score += 5

        score += skill_score

        # ---------------------------------
        # Pharma Company Bonus (10)
        # ---------------------------------
        pharma_companies = [
            "pfizer",
            "viatris",
            "abbott",
            "haleon",
            "novo nordisk",
            "biocon",
            "syngene",
            "baxter",
            "medtronic"
        ]

        if job.company.lower() in pharma_companies:
            score += 10

        # ---------------------------------
        # Location Bonus (10)
        # ---------------------------------
        if (
            "bengaluru" in job.location.lower()
            or "bangalore" in job.location.lower()
        ):
            score += 10

        # ---------------------------------
        # Experience Bonus (10)
        # ---------------------------------
        if self.profile["experience"] >= 10:
            score += 10

        # ---------------------------------
        # Save Matched Skills
        # ---------------------------------
        job.matched_skills = matched_skills

        # ---------------------------------
        # Final Score
        # ---------------------------------
        job.match_score = min(score, 100)

        # ---------------------------------
        # Recommendation
        # ---------------------------------
        if job.match_score >= 90:
            job.recommendation = "★★★★★ Excellent Match"

        elif job.match_score >= 75:
            job.recommendation = "★★★★☆ Very Good Match"

        elif job.match_score >= 60:
            job.recommendation = "★★★☆☆ Good Match"

        else:
            job.recommendation = "★★☆☆☆ Low Match"

        return job.match_score