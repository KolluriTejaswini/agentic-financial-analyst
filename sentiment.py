def get_sentiment():
    news = [
        "Stock market is growing",
        "Economic slowdown fears"
    ]

    positive_words = {"growing", "growth", "gain", "gains", "up", "bullish", "strong"}
    negative_words = {"slowdown", "fear", "fears", "loss", "losses", "down", "bearish", "weak"}

    score = 0
    for headline in news:
        words = set(headline.lower().replace(",", "").replace(".", "").split())
        pos_hits = len(words & positive_words)
        neg_hits = len(words & negative_words)

        if pos_hits > neg_hits:
            score += 1
        elif neg_hits > pos_hits:
            score -= 1

    return score / len(news)