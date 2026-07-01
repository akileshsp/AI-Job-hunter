import json
import re
from collections import OrderedDict
from pathlib import Path


class ProfileExtractor:

    TOOLS = [
        "Adobe Illustrator", "Adobe Photoshop", "Adobe Acrobat",
        "Esko Studio", "DeskPack", "WebCenter", "ArtPro",
        "ArtiosCAD", "Global Vision", "TrackWise", "Jira",
        "SAP", "Power BI", "Excel", "InDesign",

        "NetApp", "Dell EMC", "PowerMax", "VMAX", "PowerScale",
        "Isilon", "OneFS", "Commvault", "Networker",
        "ServiceNow", "Linux", "Windows Server", "VMware",
        "Azure", "AWS", "Cisco", "Brocade"
    ]

    IGNORE_WORDS = {
        "ABOUT", "PROFILE", "PHONE", "EMAIL", "ADDRESS",
        "TOTAL", "EXPERIENCE", "YEAR", "YEARS",
        "AAABBBOOOUUUTTT", "MMMEEE", "PPPRRROOOFFFIIILLLEEE",
        "CCCOOONNNTTTAAACCCTTT", "TTTOOOTTTAAALLL",
        "EEEXXXPPPEEERRRIIIEEENNNCCCEEE", "YYYEEEAAARRRSSS"
    }

    def extract(self, text):

        profile = {
            "name": "",
            "experience": 0,
            "skills": [],
            "tools": [],
            "job_titles": [],
            "industries": []
        }

        lines = [x.strip() for x in text.splitlines() if x.strip()]

        if lines:
            profile["name"] = lines[0]

        exp = re.search(r"(\d+)\+?\s*years", text, re.IGNORECASE)

        if exp:
            profile["experience"] = int(exp.group(1))

        lower = text.lower()

        # Tools
        for tool in self.TOOLS:
            if tool.lower() in lower:
                profile["tools"].append(tool)

        # Generic job title extraction
        title_regex = (
            r"(Senior\s+[A-Za-z/& -]+|"
            r"Lead\s+[A-Za-z/& -]+|"
            r"Principal\s+[A-Za-z/& -]+|"
            r"[A-Za-z/& -]+Administrator|"
            r"[A-Za-z/& -]+Engineer|"
            r"[A-Za-z/& -]+Developer|"
            r"[A-Za-z/& -]+Analyst|"
            r"[A-Za-z/& -]+Consultant|"
            r"[A-Za-z/& -]+Designer|"
            r"[A-Za-z/& -]+Specialist)"
        )

        matches = re.findall(title_regex, text, re.IGNORECASE)

        profile["job_titles"] = list(
            OrderedDict.fromkeys(
                [m.strip() for m in matches if len(m.strip()) > 5]
            )
        )

        # Skills
        words = re.findall(r"[A-Za-z][A-Za-z0-9+#./-]{3,}", text)

        skills = []

        for word in words:

            if word.upper() in self.IGNORE_WORDS:
                continue

            if re.search(r"(.)\1{3,}", word):
                continue

            skills.append(word)

        profile["skills"] = list(
            OrderedDict.fromkeys(skills)
        )[:50]

        Path("config").mkdir(exist_ok=True)

        with open(
            "config/profile_generated.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(profile, f, indent=4)

        return profile