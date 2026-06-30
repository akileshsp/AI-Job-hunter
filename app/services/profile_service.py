import json
from pathlib import Path


class ProfileService:

    def __init__(self):
        profile_path = Path("config/profile.json")

        with open(profile_path, "r", encoding="utf-8") as file:
            self.profile = json.load(file)

    def get_skills(self):
        return self.profile["skills"]

    def get_roles(self):
        return self.profile["preferred_roles"]

    def get_profile(self):
        return self.profile