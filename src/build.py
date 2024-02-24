from subprocess import run
from sys import executable

if __name__ == "__main__":
    """ Creates a python environment with the applications requirements. 
    """
    env_executable = ".venv/Scripts/python.exe"
    run([executable, "-m", "venv", ".venv"])
    run([env_executable, "-m", "pip", "install", "-r", "requirements.txt"])
    run([env_executable, "-m", "nltk.downloader", "stopwords"])
    run([env_executable, "-m", "nltk.downloader", "punkt"])
