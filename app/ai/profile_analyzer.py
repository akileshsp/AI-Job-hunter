import re


class ProfileAnalyzer:

    TOOLS = [
        "Adobe Illustrator",
        "Adobe Photoshop",
        "Esko Studio",
        "DeskPack",
        "WebCenter",
        "Jira",
        "TrackWise"
    ]

    SKILLS = [
        "Packaging Artwork",
        "Packaging",
        "Labeling",
        "Prepress",
        "Quality Control",
        "Packaging Compliance",
        "Print Production",
        "3D Packshot"
    ]

    JOB_TITLES = [
        "Packaging Designer",
        "Packaging Artwork Specialist",
        "Labeling Specialist",
        "Packaging Engineer",
        "Prepress Executive",
        "Production Executive",
        "QC Executive"
    ]

    def analyze(self, text):

        profile = {
            "name": "",
            "experience": 0,
            "skills": [],
            "tools": [],
            "job_titles": [],
            "search_queries": []
        }

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        if lines:
            profile["name"] = lines[0]

        match = re.search(r"(\d+)\+?\s*years", text, re.IGNORECASE)

        if match:
            profile["experience"] = int(match.group(1))

        lower = text.lower()

        for skill in self.SKILLS:
            if skill.lower() in lower:
                profile["skills"].append(skill)

        for tool in self.TOOLS:
            if tool.lower() in lower:
                profile["tools"].append(tool)

        for title in self.JOB_TITLES:
            if title.lower() in lower:
                profile["job_titles"].append(title)

        profile["search_queries"] = (
            profile["job_titles"]
            + profile["skills"]
            + profile["tools"]
        )

        return profile
