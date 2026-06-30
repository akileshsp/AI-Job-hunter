from app.ai.match_engine import MatchEngine
from app.models.job import Job

matcher = MatchEngine()

jobs = [

    Job(
        title="Senior Packaging Specialist",
        company="Pfizer",
        location="Bengaluru",
        source="Test",
        url=""
    ),

    Job(
        title="Packaging Artwork Specialist",
        company="Viatris",
        location="Bengaluru",
        source="Test",
        url=""
    ),

    Job(
        title="Java Developer",
        company="Google",
        location="Bengaluru",
        source="Test",
        url=""
    )

]

print("\nAI MATCH SCORES\n")

for job in jobs:

    score = matcher.calculate_score(job)

    print(job.title)
    print(score)
    print()