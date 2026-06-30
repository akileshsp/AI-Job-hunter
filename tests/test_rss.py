from app.utils.rss_reader import RSSReader

rss = RSSReader.read(
    "https://stackoverflow.com/jobs/feed"
)

print(len(rss.entries))