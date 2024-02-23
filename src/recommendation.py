from scholarly import scholarly, ProxyGenerator, MaxTriesExceededException, Publication
from time import sleep
from numpy import clip, sort

from requests import get as fetch
from PyPDF2 import PdfReader
from re import sub as replace


MAX_PUBS = 10
""" Defines the maximun number of publications to be requested at once.
"""
SLEEP_TIMER = 6
""" Defines the number of seconds between each publication request.
"""


def next_publication(publications: iter) -> Publication:
    """ Given a publication iterable, sleeps the application for some time and returns the next publication.
    """
    sleep(SLEEP_TIMER)
    return next(publications)


def search_pubs(query: str) -> list():
    """ Given a topic, returns a list of Publication type objects.
    """
    # 1.- Find available publications on topic.
    try:
        publications = scholarly.search_pubs(query)
    # 2.- Validate if IP is blocked.
    except MaxTriesExceededException as max_tries:
        total_results = -1
    # 3.- Iterate over publication results.
    else:
        total_results = 0 if publications.total_results == None else publications.total_results
    return None if total_results == -1 else [next_publication(publications) for _ in range(clip(MAX_PUBS, 0, total_results))]


def best_publication(pubs: list()) -> Publication:
    """ Given a list of Publication type objects, returns the publication with the best score.
    """
    # 1.- Validate existing publication array
    if len(pubs) == 0:
        return None
    # 2.- Store an ordered list of publications score, based on Google's rank and number of citations
    best = None
    true_rank = [1 / pubs[i]['gsrank'] * 1000 + pubs[i]['num_citations'] for i in range(len(pubs))]
    true_rank_sorted = sort(true_rank)[::-1]
    # 3.- The best publication must have eprint_url attribute, and must be a pdf
    for score in true_rank_sorted:
        index = true_rank.index(score)
        if 'eprint_url' in pubs[index] and pubs[index]['eprint_url'].endswith(".pdf"):
            best = pubs[index]
            break
    # 4.- Fetch all data of the best Publication
    if best != None:
        best = scholarly.fill(best)
    # 5.- Clean data
    best['bib']['pdf_title'] = replace(r'[<>:"/\\|?*]', '_', best['bib']['title'])
    return best


def fetch_pdf_data(publication: Publication) -> None:
    """ Given a publication, fetches the pdf from its associated url.
    """
    with open(f"data/pdf/{publication['bib']['pdf_title']}.pdf", 'wb') as pdf_file:
        response = fetch(publication['eprint_url'])
        pdf_file.write(response.content)


def parse_pdf_data(publication: Publication) -> str:
    """ Given a publication, parses data that has been stored at data/pdf/{name} and returns its text formated.
    """
    with open(f"data/pdf/{publication['bib']['pdf_title']}.pdf", 'rb') as pdf_file:
        # Read pdf file
        reader = PdfReader(pdf_file)
        text = '\n'.join([page.extract_text() for page in reader.pages])
        # Format the resulting text
        text = text.replace('-\n', '')
        text = text.replace('.', '.\n')
        text = text.replace(' \n', ' ')
    return text