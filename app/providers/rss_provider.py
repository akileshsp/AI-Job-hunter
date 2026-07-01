from app.providers.base_provider import BaseProvider
from app.models.job import Job
from app.utils.rss_reader import RSSReader


class RSSProvider(BaseProvider):

    def search(self):

        jobs = []

        feeds = [
            "https://stackoverflow.com/jobs/feed"
        ]

        for feed in feeds:

            data = RSSReader.read(feed)

            for item in data.entries:

                jobs.append(
                    Job(
                        title=item.title,
                        company="RSS Feed",
                        location="Unknown",
                        source="RSS",
                        url=item.link,
                        description=getattr(item, "summary", "")
                    )
                )

        return jobs