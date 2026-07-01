import json
import re
from collections import OrderedDict
from pathlib import Path


class ProfileExtractor:

    TOOLS = [
        "Adobe Illustrator",
        "Adobe Photoshop",
        "Adobe Acrobat",
        "Esko Studio",
        "DeskPack",
        "WebCenter",
        "ArtPro",
        "ArtiosCAD",
        "Global Vision",
        "TrackWise",
        "Jira",
        "SAP",
        "Power BI",
        "Excel",
        "InDesign"
    ]

    INDUSTRIES = [
        "Pharmaceutical",
        "Packaging",
        "Medical Device",
        "FMCG",
        "Printing",
        "Food",
        "Healthcare"
    ]

    JOB_PATTERNS = [
        r"Senior\s+Packaging\s+[\w\s]+",
        r"Packaging\s+Designer",
        r"Packaging\s+Engineer",
        r"Packaging\s+Specialist",
        r"Packaging\s+Artwork\s+Specialist",
        r"Artwork\s+Specialist",
        r"Labeling\s+Specialist",
        r"Prepress\s+Executive",
        r"Production\s+Executive",
        r"QC\s+Executive"
    ]

    def extract(self, text: str):

        profile = {
            "name": "",
            "experience": 0,
            "skills": [],
            "tools": [],
            "job_titles": [],
            "industries": []
        }

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        if lines:
            profile["name"] = lines[0]

        lower = text.lower()

        exp = re.search(r"(\d+)\+?\s*years", lower)

        if exp:
            profile["experience"] = int(exp.group(1))

        words = re.findall(r"[A-Za-z][A-Za-z0-9&+.#/-]{2,}", text)

        stop_words = {
            "with", "from", "that", "this", "your", "have",
            "will", "years", "year", "worked", "work",
            "using", "experience", "specialist"
        }

        skills = []

        for word in words:

            w = word.strip()

            if len(w) < 4:
                continue

            if w.lower() in stop_words:
                continue

            if w.isupper():
                skills.append(w)

            elif w[0].isupper():
                skills.append(w)

        profile["skills"] = list(
            OrderedDict.fromkeys(skills)
        )

        for tool in self.TOOLS:

            if tool.lower() in lower:
                profile["tools"].append(tool)

        for industry in self.INDUSTRIES:

            if industry.lower() in lower:
                profile["industries"].append(industry)

        for pattern in self.JOB_PATTERNS:

            for match in re.findall(pattern, text, re.IGNORECASE):
                profile["job_titles"].append(match.strip())

        profile["skills"] = profile["skills"][:40]
        profile["tools"] = list(OrderedDict.fromkeys(profile["tools"]))
        profile["industries"] = list(OrderedDict.fromkeys(profile["industries"]))
        profile["job_titles"] = list(OrderedDict.fromkeys(profile["job_titles"]))

        Path("config").mkdir(exist_ok=True)

        with open(
            "config/profile_generated.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(profile, f, indent=4)

        return profile