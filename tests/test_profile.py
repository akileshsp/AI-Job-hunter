from app.ai.profile_analyzer import ProfileAnalyzer
from app.ai.resume_parser import ResumeParser

parser = ResumeParser()
analyzer = ProfileAnalyzer()

text = parser.parse("resume/resume.pdf")

profile = analyzer.analyze(text)

print("\n========== PROFILE ==========\n")

for key, value in profile.items():
    print(f"{key}:")
    print(value)
    print()