from app.services.profile_service import ProfileService


class MatchEngine:

    def __init__(self):
        profile = ProfileService()
        self.skills = profile.get_skills()

    def calculate_score(self, title: str) -> int:
        score = 50

        title_lower = title.lower()

        for skill in self.skills:
            if skill.lower() in title_lower:
                score += 10

        return min(score, 100)