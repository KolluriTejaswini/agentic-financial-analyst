import requests
from transformers import pipeline

API_KEY = "64e143b304be489ea2adf2ae99cb77a6"

sentiment_model = pipeline("sentiment-analysis")

def get_sentiment(stock):

    url = f"https://newsapi.org/v2/everything?q={stock}&apiKey={API_KEY}"
    response = requests.get(url)
    articles = response.json()["articles"][:5]

    headlines = [article["title"] for article in articles]

    if not headlines:
        return 0

    results = sentiment_model(headlines)

    score = 0
    for r in results:
        if r['label'] == 'POSITIVE':
            score += 1
        else:
            score -= 1

    return score / len(results)