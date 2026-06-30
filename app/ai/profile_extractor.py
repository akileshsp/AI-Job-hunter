import json
import re
from pathlib import Path


class ProfileExtractor:

    SKILLS = [
        "Packaging Artwork",
        "Packaging",
        "Labeling",
        "Regulatory Packaging",
        "Esko Studio",
        "DeskPack",
        "WebCenter",
        "Adobe Illustrator",
        "Adobe Photoshop",
        "Jira",
        "TrackWise",
        "Prepress",
        "3D Packshot",
        "QC"
    ]

    COMPANIES = [
        "Viatris",
        "Mylan",
        "SGK",
        "Schawk",
        "SGSCO",
        "Sun Branding",
        "Stirred Creative"
    ]

    def extract(self, text: str):

        profile = {
            "name": "",
            "experience": 0,
            "skills": [],
            "companies": []
        }

        # Name
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if lines:
            profile["name"] = lines[0]

        # Experience
        match = re.search(r"(\d+)\+?\s*years", text, re.IGNORECASE)
        if match:
            profile["experience"] = int(match.group(1))

        # Skills
        lower = text.lower()
        for skill in self.SKILLS:
            if skill.lower() in lower:
                profile["skills"].append(skill)

        # Companies
        for company in self.COMPANIES:
            if company.lower() in lower:
                profile["companies"].append(company)

        Path("config").mkdir(exist_ok=True)

        with open("config/profile_generated.json", "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=4)

        return profile