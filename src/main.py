from recommendation import search_pubs, best_publication, fetch_pdf_data, parse_pdf_data
from natural_language import NaturalLanguange
from json import dumps as save_json


def input_valid_language() -> str:
    """ Prompt user to input a language, and returns it once a valid language was selected.
        User can also type quit.
    """
    print('Type "quit" to exit translation process.')
    language = input("Select a valid language: ").lower()
    while(language != 'quit' and not NaturalLanguange.is_valid_language(language)):
        language = input(f"There's no support for {language}. Select a valid Language: ").lower()
    return language


def create_txt(content: str, article: str, lan: str = 'default') -> str:
    """ Creates a text file at 'out' directory with its corresponding content.
        Returns file path
    """
    article = article.replace(' ', '_')
    tag_name = f'summary_{lan}'
    file_name = f'out/{article}_{tag_name}.txt'
    with open(f'{file_name}', 'w', encoding='utf-8') as summary_file:
        summary_file.write(content)
    return file_name

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


if __name__ == '__main__':
    # Query the user for a topic
    nl = NaturalLanguange("english")
    query = input("What topic do you whant to search? ")
    print("\nSearching for publications...")
    pubs = search_pubs(query)

    if pubs == None:
        print(f"To many tries. Try in two days time.")
    elif len(pubs) == 0:
        print(f"{query} is unavailable. Try an other subject.")
    else:
        # 0.- Save publication
        save_pubs(pubs, f"{query}")
        # 1.- Generate recomendation
        print("Picking the best publication...")
        best = best_publication(pubs)
        article_name = best['bib']['pdf_title']
        print(f"Best article found is: '{article_name}'.")
        print(f"Link: {best['eprint_url']}.")
        print("Fetching data...")
        fetch_pdf_data(best)
        print("Parsing data...")
        text = parse_pdf_data(best)
        # 2.- Summerize text
        print(f"\nSummarizing its contents...")
        summary = f"Abstract:\n{best['bib']['abstract']}\nContent:\n{nl.text_reduction(text)}"
        summary_path = create_txt(summary, article_name)
        print(f'Saved summary at {summary_path}')
        summary_data = {'default': summary}
        # 3.- Translate summary
        print(f'\nAvailable languages: {NaturalLanguange.dictionaries.keys()}')
        target_lan = input_valid_language()
        while target_lan.lower() != 'quit':
            print(f"Translating document to {target_lan}...")
            translated_text = NaturalLanguange.translate(summary, target_lan)
            translate_path = create_txt(translated_text, article_name, target_lan)
            summary_data[target_lan] = translated_text
            print(f"Saved translation at: {translate_path}")
            target_lan = input_valid_language()
        # 4.- Save all summaries
        save_summaries(summary_data, query)
        print("Thanks for using GSpy!")
