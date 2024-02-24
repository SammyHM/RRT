from json import dumps as save_json
from PyPDF2 import PdfReader


JSON_PATH = "data/json"
""" Defines the file location where all json files are stored.
"""
PDF_PATH = "data/pdf"
""" Defines the file location where all pdf files are stored.
"""

def create_txt(content: str, article: str, lan: str = 'default') -> str:
    """ Creates a text file at 'out' directory with its corresponding content.
        Returns file path.
    """
    article = article.replace(' ', '_')
    tag_name = f'summary_{lan}'
    file_path = f'out/{article}_{tag_name}.txt'
    with open(f'{file_path}', 'w', encoding='utf-8') as summary_file:
        summary_file.write(content)
    return file_path

def save_pubs(pubs: list(), name: str) -> None:
    """ Given a list of Publication type objects, saves a json file representative of it.
    """
    json = save_json(pubs, indent=4)
    with open(f"{JSON_PATH}/query/{name}.json", "w") as json_file:
        json_file.write(json)


def save_summaries(pubs: list(), name: str) -> None:
    """ Given a list of summaries, saves a json file representative of it.
    """
    json = save_json(pubs, indent=4)
    with open(f"{JSON_PATH}/summary/{name}.json", "w") as json_file:
        json_file.write(json)


def write_pdf_data(file_name: str, content: bytes) -> None:
    """ Given a file name, saves the content at pdf data path.
    """
    with open(f"{PDF_PATH}/{file_name}.pdf", 'wb') as pdf_file:
        pdf_file.write(content)


def parse_pdf_data(file_name:str) -> str:
    """ Given a file_name, parses its pdf data and returns its text formated.
    """
    with open(f"{PDF_PATH}/{file_name}.pdf", 'rb') as pdf_file:
        # Read pdf file
        reader = PdfReader(pdf_file)
        text = '\n'.join([page.extract_text() for page in reader.pages])
        # Format the resulting text
        text = text.replace('-\n', '')
        text = text.replace('.', '.\n')
        text = text.replace(' \n', ' ')
    return text
