import feedparser


class RSSReader:

    @staticmethod
    def read(url):

        print(f"📡 Reading RSS: {url}")

        return feedparser.parse(url)