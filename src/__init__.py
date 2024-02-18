from setuptools import setup, find_packages

setup(
    name='GSpy',
    version='1.0.4',
    packages=find_packages(),
)

# Install nltk dependencies
from nltk import download, data
if not data.find('corpora/stopwords.zip'):
    download('stopwords')

if not data.find('corpora/punkt.zip'):
    download('punkt')
