from app.database.job_repository import (
    save_job,
    save_for_user,
    get_saved_jobs
)


class SavedJobsService:

    def save(self, user_id, job):

        job_id = save_job(job)

        save_for_user(
            user_id,
            job_id
        )

    def get_saved_jobs(self, user_id):

        return get_saved_jobs(user_id)