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

        title = job.title.lower()

        # Match resume skills with job title
        for skill in self.profile["skills"]:
            if skill.lower() in title:
                score += 10

        # Pharma company bonus
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
            score += 20

        # Bengaluru bonus
        if "bengaluru" in job.location.lower() or "bangalore" in job.location.lower():
            score += 10

        # Experience bonus
        if self.profile["experience"] >= 10:
            score += 10

        return min(score, 100)