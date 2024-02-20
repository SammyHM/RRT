from subprocess import run
from sys import executable

if __name__ == "__main__":
    run([executable, "venv", ".venv"])
    run([executable, "pip", "install", "requirements.txt"])
    run([executable, "nltk.downloader", "stopwords"])
    run([executable, "nltk.downloader", "punkt"])
