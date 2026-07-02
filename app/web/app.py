from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash
)

import os

from app.auth.auth_service import AuthService
from app.providers.real_job_provider import RealJobProvider
from app.database.job_repository import total_jobs
from app.services.profile_service import ProfileService
from app.services.saved_jobs_service import SavedJobsService
from app.models.job import Job

app = Flask(__name__)

app.secret_key = "ai-job-hunter-secret"

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

auth = AuthService()

saved_jobs = SavedJobsService()


@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    profile_exists = os.path.exists(
        f"uploads/profiles/{session['user']['id']}.json"
    )

    return render_template(
        "index.html",
        user=session["user"],
        total_jobs=total_jobs(),
        profile_ready=profile_exists
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        success, message = auth.register(
            request.form["name"],
            request.form["email"],
            request.form["password"]
        )

        if success:

            flash("Registration successful. Please login.")

            return redirect("/login")

        flash(message)

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        success, user = auth.login(
            request.form["email"],
            request.form["password"]
        )

        if success:

            session["user"] = dict(user)

            return redirect("/")

        flash("Invalid email or password.")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


@app.route("/upload", methods=["POST"])
def upload():

    if "user" not in session:
        return redirect("/login")

    file = request.files.get("resume")

    if not file or not file.filename:

        flash("Please choose a PDF resume.")

        return redirect("/")

    user_id = session["user"]["id"]

    user_folder = os.path.join(
        UPLOAD_FOLDER,
        str(user_id)
    )

    os.makedirs(
        user_folder,
        exist_ok=True
    )

    resume_path = os.path.join(
        user_folder,
        "resume.pdf"
    )

    file.save(resume_path)

    try:

        ProfileService(user_id)

        flash("Resume uploaded and AI profile generated successfully.")

    except Exception as e:

        flash(f"Profile generation failed: {e}")

    return redirect("/")


@app.route("/results")
def results():

    if "user" not in session:
        return redirect("/login")

    keyword = request.args.get(
        "keyword",
        ""
    )

    location = request.args.get(
        "location",
        "Bengaluru"
    )

    provider = RealJobProvider(
        session["user"]["id"]
    )

    jobs = provider.search(
        keyword=keyword,
        location=location
    )

    jobs.sort(
        key=lambda j: getattr(
            j,
            "match_score",
            0
        ),
        reverse=True
    )

    return render_template(
        "results.html",
        jobs=jobs,
        keyword=keyword,
        location=location,
        total_jobs=total_jobs(),
        user=session["user"]
    )


@app.route("/save")
def save_job():

    if "user" not in session:
        return redirect("/login")

    job = Job(
        title=request.args.get("title", ""),
        company=request.args.get("company", ""),
        location=request.args.get("location", ""),
        source=request.args.get("source", ""),
        url=request.args.get("url", ""),
        description=""
    )

    saved_jobs.save(
        session["user"]["id"],
        job
    )

    flash("Job saved successfully.")

    return redirect("/saved")


@app.route("/saved")
def saved():

    if "user" not in session:
        return redirect("/login")

    jobs = saved_jobs.get_saved_jobs(
        session["user"]["id"]
    )

    return render_template(
        "saved_jobs.html",
        jobs=jobs,
        user=session["user"]
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )