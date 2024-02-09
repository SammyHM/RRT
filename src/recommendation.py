# pip install scholarly
# pip install numpy
from scholarly import scholarly, ProxyGenerator, MaxTriesExceededException, Publication
from numpy import clip, sort

# pip install PyPDF2
from requests import get as fetch
from PyPDF2 import PdfReader
from re import sub as replace


MAX_PUBS = 30


def search_pubs(query: str) -> list():
    """ Given a topic, returns a list of Publication type objects
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
    return None if total_results == -1 else [next(publications) for _ in range(clip(MAX_PUBS, 0, total_results))]


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
    # if best != None:
    #     best = scholarly.fill(best)
    # 5.- Clean data
    best['bib']['pdf_title'] = replace(r'[<>:"/\\|?*]', '_', best['bib']['title'])
    return best


def fetch_pdf_data(publication: Publication) -> str:
    """ Given a publication, fetches data from the url and writes it to local file.
        Returns the text found in the pdf
    """
    with open(f"data/{publication['bib']['pdf_title']}.pdf", 'w+b') as pdf_file:
        # Create pdf file and fill content
        response = fetch(publication['eprint_url'])
        pdf_file.write(response.content)
        # Read pdf file
        reader = PdfReader(pdf_file)
        text = '\n'.join([page.extract_text() for page in reader.pages])
        # Format the resulting text
        text = text.replace('-\n', '')
        text = text.replace('.', '.\n')
        text = replace(r'[\sa-zA-Z]\n', ' ', text)
        
    return text