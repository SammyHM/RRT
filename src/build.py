from subprocess import run
from sys import executable

if __name__ == "__main__":
    """ Creates a python environment with the applications requirements. 
    """
    run([executable, "-m", "venv", ".venv"])
    run([executable, "-m", "pip", "install", "-r", "requirements.txt"])
    run([executable, "-m", "nltk.downloader", "stopwords"])
    run([executable, "-m", "nltk.downloader", "punkt"])
