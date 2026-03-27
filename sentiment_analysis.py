from transformers import pipeline

sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_sentiment(text):
    return sentiment_analyzer(text)
