import re
from textblob import TextBlob

class TextProcessor:
    def __init__(self):
        pass

    def clean_text(self, text):
        """Clean and preprocess text."""
        # Convert to lowercase
        text = text.lower()
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text

    def tokenize(self, text):
        """Tokenize text into words using simple split."""
        return text.split()

    def process_text(self, text):
        """Complete text processing pipeline using only TextBlob and basic Python."""
        cleaned_text = self.clean_text(text)
        # TextBlob for lemmatization
        blob = TextBlob(cleaned_text)
        tokens = [word.lemmatize() for word in blob.words]
        return ' '.join(tokens)

    def get_sentiment(self, text):
        """Get sentiment analysis using TextBlob."""
        blob = TextBlob(text)
        return {
            'polarity': blob.sentiment.polarity,  # Range: -1 to 1
            'subjectivity': blob.sentiment.subjectivity,  # Range: 0 to 1
            'sentiment': 'positive' if blob.sentiment.polarity > 0 else 'negative' if blob.sentiment.polarity < 0 else 'neutral'
        }

    def get_emotion_keywords(self, text):
        """Extract emotion-related keywords from text using simple split."""
        emotion_keywords = {
            'joy': ['happy', 'joy', 'excited', 'delighted', 'pleased'],
            'sadness': ['sad', 'unhappy', 'depressed', 'miserable', 'gloomy'],
            'anger': ['angry', 'furious', 'annoyed', 'irritated', 'frustrated'],
            'fear': ['afraid', 'scared', 'fearful', 'anxious', 'worried'],
            'surprise': ['surprised', 'amazed', 'astonished', 'shocked'],
            'neutral': ['okay', 'fine', 'normal', 'average', 'regular']
        }
        tokens = self.tokenize(text.lower())
        emotions = {}
        for emotion, keywords in emotion_keywords.items():
            count = sum(1 for token in tokens if token in keywords)
            if count > 0:
                emotions[emotion] = count
        return emotions 