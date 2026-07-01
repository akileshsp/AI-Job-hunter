from dataclasses import dataclass, field


@dataclass(slots=True)
class Job:
    title: str
    company: str
    location: str
    source: str
    url: str

    description: str = ""
    posted_date: str = ""
    employment_type: str = ""

    match_score: float = 0.0
    matched_skills: list[str] = field(default_factory=list)
    missing_skills: list[str] = field(default_factory=list)

    recommendation: str = ""

    salary: str = ""
    experience: str = ""
    department: str = ""
    remote: bool = False

    def unique_key(self) -> str:
        return (
            f"{self.company.strip().lower()}|"
            f"{self.title.strip().lower()}|"
            f"{self.url.strip().lower()}"
        )

    def update_score(
        self,
        score: float,
        matched_skills=None,
        recommendation=""
    ):
        self.match_score = round(score, 2)

        if matched_skills:
            self.matched_skills = matched_skills

        if recommendation:
            self.recommendation = recommendation

    def __hash__(self):
        return hash(self.unique_key())