from setuptools import setup, find_packages

setup(
    name="workplace-sentiment-analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'nltk==3.8.1',
        'pandas>=2.2.0',
        'textblob==0.17.1',
        'matplotlib>=3.10.0',
        'seaborn>=0.12.0',
        'numpy>=2.2.0',
    ],
    python_requires='>=3.8',
) 