@echo off
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing wheel and setuptools...
pip install wheel setuptools

echo Installing dependencies...
pip install -e .

echo Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger'); nltk.download('wordnet')"

echo Installation complete!
pause 