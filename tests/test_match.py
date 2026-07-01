from app.ai.match_engine import MatchEngine
from app.models.job import Job

matcher = MatchEngine()

jobs = [

    Job(
        title="Senior Packaging Artwork Specialist",
        company="Viatris",
        location="Bengaluru",
        source="Test",
        url="",
        description="""
        Pharmaceutical packaging artwork.
        Labeling.
        Regulatory packaging.
        Esko Studio.
        Adobe Illustrator.
        DeskPack.
        WebCenter.
        Prepress.
        Packaging compliance.
        Packaging lifecycle.
        """
    ),

    Job(
        title="Packaging Designer",
        company="Abbott",
        location="Bengaluru",
        source="Test",
        url="",
        description="""
        Packaging artwork creation.
        Adobe Illustrator.
        Packaging.
        Labeling.
        Print production.
        Prepress.
        """
    ),

    Job(
        title="Java Developer",
        company="Google",
        location="Bengaluru",
        source="Test",
        url="",
        description="""
        Java
        Spring Boot
        Kubernetes
        React
        AWS
        """
    )

]

print("\n========== AI MATCH TEST ==========\n")

for job in jobs:

    matcher.calculate_score(job)

    print(f"Role     : {job.title}")
    print(f"Company  : {job.company}")
    print(f"Score    : {job.match_score}")
    print(f"Matched  : {job.matched_skills}")
    print(f"Advice   : {job.recommendation}")
    print("-" * 60)