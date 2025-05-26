import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import argparse
from text_processor import TextProcessor
import numpy as np
import os

class WorkplaceSentimentAnalyzer:
    def __init__(self):
        self.text_processor = TextProcessor()
        
    def load_data(self, file_path):
        """Load and preprocess the input data."""
        try:
            df = pd.read_csv(file_path, skip_blank_lines=True)
            required_columns = ['text', 'timestamp']
            if not all(col in df.columns for col in required_columns):
                raise ValueError(f"CSV must contain columns: {required_columns}")
            # Strip whitespace from timestamps
            df['timestamp'] = df['timestamp'].astype(str).str.strip()
            # Convert timestamp to datetime, coerce errors
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', format='%Y-%m-%d')
            # Drop rows with invalid timestamps
            df = df.dropna(subset=['timestamp'])
            return df
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None

    def analyze_sentiment(self, df):
        """Analyze sentiment for all entries in the dataset."""
        df['processed_text'] = df['text'].apply(self.text_processor.process_text)
        df['sentiment_scores'] = df['text'].apply(self.text_processor.get_sentiment)
        df['emotions'] = df['text'].apply(self.text_processor.get_emotion_keywords)
        
        # Extract sentiment components
        df['polarity'] = df['sentiment_scores'].apply(lambda x: x['polarity'])
        df['subjectivity'] = df['sentiment_scores'].apply(lambda x: x['subjectivity'])
        df['sentiment'] = df['sentiment_scores'].apply(lambda x: x['sentiment'])
        
        return df

    def generate_visualizations(self, df, output_dir='.'):
        """Generate and save visualizations of the analysis results."""
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        # Set style
        plt.style.use('seaborn-v0_8')
        
        # 1. Sentiment Distribution
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='sentiment')
        plt.title('Distribution of Sentiment Categories')
        plt.savefig(f'{output_dir}/sentiment_distribution.png')
        plt.close()
        
        # 2. Sentiment Over Time
        plt.figure(figsize=(12, 6))
        df.set_index('timestamp')['polarity'].rolling(window=7).mean().plot()
        plt.title('Sentiment Trend Over Time (7-day rolling average)')
        plt.xlabel('Date')
        plt.ylabel('Sentiment Polarity')
        plt.savefig(f'{output_dir}/sentiment_trend.png')
        plt.close()
        
        # 3. Emotion Distribution
        emotion_counts = pd.DataFrame([emotion for emotions in df['emotions'] for emotion in emotions.items()],
                                    columns=['emotion', 'count'])
        plt.figure(figsize=(10, 6))
        sns.barplot(data=emotion_counts, x='emotion', y='count')
        plt.title('Distribution of Emotions')
        plt.xticks(rotation=45)
        plt.savefig(f'{output_dir}/emotion_distribution.png')
        plt.close()

    def generate_report(self, df, output_file='sentiment_report.txt'):
        """Generate a text report of the analysis results."""
        with open(output_file, 'w') as f:
            f.write("Workplace Sentiment Analysis Report\n")
            f.write("=================================\n\n")
            
            # Overall sentiment distribution
            sentiment_dist = df['sentiment'].value_counts()
            f.write("Overall Sentiment Distribution:\n")
            for sentiment, count in sentiment_dist.items():
                f.write(f"{sentiment}: {count} entries ({count/len(df)*100:.1f}%)\n")
            f.write("\n")
            
            # Average sentiment scores
            f.write("Average Sentiment Scores:\n")
            f.write(f"Polarity: {df['polarity'].mean():.2f}\n")
            f.write(f"Subjectivity: {df['subjectivity'].mean():.2f}\n\n")
            
            # Most common emotions
            emotion_counts = pd.DataFrame([emotion for emotions in df['emotions'] for emotion in emotions.items()],
                                        columns=['emotion', 'count'])
            f.write("Most Common Emotions:\n")
            for emotion, count in emotion_counts.groupby('emotion')['count'].sum().sort_values(ascending=False).items():
                f.write(f"{emotion}: {count} occurrences\n")

def main():
    parser = argparse.ArgumentParser(description='Workplace Sentiment Analysis')
    parser.add_argument('--input', required=True, help='Path to input CSV file')
    parser.add_argument('--output-dir', default='.', help='Output directory for visualizations')
    args = parser.parse_args()
    
    analyzer = WorkplaceSentimentAnalyzer()
    
    # Load and analyze data
    df = analyzer.load_data(args.input)
    if df is not None:
        df = analyzer.analyze_sentiment(df)
        
        # Generate visualizations
        analyzer.generate_visualizations(df, args.output_dir)
        
        # Generate report
        analyzer.generate_report(df)
        
        print("Analysis complete! Check the output directory for results.")

if __name__ == "__main__":
    main() 