from flask import Flask, render_template, request

from app.providers.real_job_provider import RealJobProvider
from app.database.job_repository import total_jobs

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html",
        total_jobs=total_jobs()
    )


@app.route("/results")
def results():

    keyword = request.args.get(
        "keyword",
        "Packaging Designer"
    )

    location = request.args.get(
        "location",
        "Bengaluru"
    )

    provider = RealJobProvider()

    provider.keywords = [keyword]
    provider.locations = [location]

    jobs = provider.search()

    jobs.sort(
        key=lambda job: getattr(job, "match_score", 0),
        reverse=True
    )

    return render_template(
        "results.html",
        jobs=jobs,
        keyword=keyword,
        location=location,
        total_jobs=total_jobs()
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )