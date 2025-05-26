# AI-Powered Sentiment Analysis for Workplace Wellness

This project implements an AI-powered sentiment analysis system designed to monitor and analyze workplace wellness through employee feedback and communications.

## Features

- Sentiment analysis of employee feedback
- Emotion detection in workplace communications
- Trend analysis of workplace sentiment over time
- Visualization of sentiment patterns
- Support for multiple text input formats

## Setup Instructions

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download required NLTK data:
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger'); nltk.download('wordnet')"
   ```

## Project Structure

- `sentiment_analyzer.py`: Main sentiment analysis implementation
- `text_processor.py`: Text preprocessing utilities
- `sample_data.csv`: Sample employee feedback data
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## Usage

1. Prepare your input data in CSV format with columns for text and timestamps
2. Run the sentiment analyzer:
   ```bash
   python sentiment_analyzer.py --input your_data.csv
   ```

## Output

The system generates:
- Sentiment scores for each feedback entry
- Emotion analysis results
- Trend visualizations
- Summary reports

## Contributing

Feel free to submit issues and enhancement requests! 