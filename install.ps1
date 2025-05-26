# Ensure we're using PowerShell
if ($PSVersionTable.PSVersion.Major -lt 5) {
    Write-Host "This script requires PowerShell 5.0 or higher"
    exit 1
}

# Function to check if a command exists
function Test-Command($cmdname) {
    return [bool](Get-Command -Name $cmdname -ErrorAction SilentlyContinue)
}

# Check if Python is installed
if (-not (Test-Command python)) {
    Write-Host "Python is not installed or not in PATH"
    exit 1
}

Write-Host "Creating virtual environment..."
if (Test-Path venv) {
    Remove-Item -Recurse -Force venv
}
python -m venv venv

Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "Installing build tools..."
pip install --upgrade wheel setuptools

Write-Host "Installing dependencies in order..."
# Install numpy first as it's a dependency for other packages
pip install numpy --only-binary :all:

# Install other packages
pip install pandas --only-binary :all:
pip install matplotlib --only-binary :all:
pip install seaborn --only-binary :all:
pip install nltk==3.8.1
pip install textblob==0.17.1

Write-Host "Downloading NLTK data..."
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('averaged_perceptron_tagger', quiet=True); nltk.download('wordnet', quiet=True); nltk.download('stopwords', quiet=True)"

Write-Host "Testing installation..."
python -c "import nltk; import pandas; import numpy; import matplotlib; import seaborn; import textblob; print('All packages imported successfully!')"

Write-Host "Installation complete!"
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 