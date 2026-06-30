from dataclasses import dataclass, field


@dataclass
class Job:

    title: str
    company: str
    location: str
    source: str
    url: str

    description: str = ""
    posted_date: str = ""
    employment_type: str = ""

    match_score: int = 0
    matched_skills: list = field(default_factory=list)

    recommendation: str = ""