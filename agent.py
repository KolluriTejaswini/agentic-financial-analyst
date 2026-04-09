def decision(predicted, current, sentiment):
    # Convert to scalar if values come as Pandas Series / NumPy arrays
    if hasattr(predicted, "item"):
        predicted = predicted.item()
    if hasattr(current, "item"):
        current = current.item()
    if hasattr(sentiment, "item"):
        sentiment = sentiment.item()

    # Decision logic
    if predicted > current and sentiment > 0:
        return "BUY"
    elif predicted < current and sentiment < 0:
        return "SELL"
    else:
        return "HOLD"