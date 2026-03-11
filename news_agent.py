import feedparser

class NewsAgent:

    def fetch_news(self, ticker):

        url = f"https://news.google.com/rss/search?q={ticker}+stock"

        feed = feedparser.parse(url)

        headlines = []

        for entry in feed.entries[:5]:
            headlines.append(entry.title)

        return headlines

    def analyze_sentiment(self, headlines):

        positive_words = ["growth", "profit", "gain", "rise", "surge"]
        negative_words = ["loss", "fall", "drop", "decline", "crash"]

        score = 0

        for headline in headlines:
            text = headline.lower()

            for word in positive_words:
                if word in text:
                    score += 1

            for word in negative_words:
                if word in text:
                    score -= 1

        if score > 0:
            return "Positive"
        elif score < 0:
            return "Negative"
        else:
            return "Neutral"