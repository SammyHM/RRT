from json import dumps as save_json


def create_txt(content: str, article: str, lan: str = 'default') -> str:
    """ Creates a text file at 'out' directory with its corresponding content.
        Returns file path
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
    with open(f"data/json/query/{name}.json", "w") as json_file:
        json_file.write(json)


def save_summaries(pubs: list(), name: str) -> None:
    """ Given a list of summaries, saves a json file representative of it.
    """
    json = save_json(pubs, indent=4)
    with open(f"data/json/summary/{name}.json", "w") as json_file:
        json_file.write(json)