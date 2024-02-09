from pub_test import PUB_TEST
from recommendation import search_pubs, best_publication, fetch_pdf_data
from natural_language import NaturalLanguange


def input_valid_language() -> str:
    """ Prompt user to input a language, and returns it once a valid language was selected.
        User can also type quit.
    """
    print('Type "quit" to exit translation process.')
    language = input("Select a valid language: ").lower()
    while(language != 'quit' and not NaturalLanguange.is_valid_language(language)):
        language = input(f"There's no support for {language}. Select a valid Language: ").lower()
    return language


def create_file(content: str, article: str, lan: str = 'default') -> str:
    """ Creates a text file at 'out' directory with its corresponding content.
        Returns file path
    """
    article = article.replace(' ', '_')
    tag_name = f'summary_{lan}'
    file_name = f'out/{article}_{tag_name}.txt'
    with open(f'{file_name}', 'w', encoding='utf-8') as summary_file:
        summary_file.write(content)
    return file_name


if __name__ == '__main__':
    # Query the user for a topic
    nl = NaturalLanguange("english")
    query = input("What topic do you whant to search? ")
    print("\nSearching for publications...")
    # pubs = search_pubs(query)
    pubs = PUB_TEST

    if pubs == None:
        print(f"To many tries. Try in two days time.")
    elif len(pubs) == 0:
        print(f"{query} is unavailable. Try an other subject.")
    else:
        # 1.- Generate recomendation
        print("Picking the best publication...")
        best = best_publication(pubs)
        article_name = best['bib']['pdf_title']
        print(f"Best article found is: '{article_name}'.")
        print(f"Link: {best['eprint_url']}.")
        print("Fetching data...")
        text = fetch_pdf_data(best)
        # 2.- Summerize text
        print(f"\nSummarizing its contents...")
        summary = f"Abstract:\n{best['bib']['abstract']}\n{nl.text_reduction(text)}"
        summary_path = create_file(summary, article_name)
        print(f'Saved summary at {summary_path}')
        # 3.- Translate summary
        print(f'\nAvailable languages: {NaturalLanguange.dictionaries.keys()}')
        target_lan = input_valid_language()
        while target_lan.lower() != 'quit':
            print(f"Translating document to {target_lan}...")
            translated_text = NaturalLanguange.translate(summary, target_lan)
            translate_path = create_file(translated_text, article_name, target_lan)
            print(f"Saved translation at: {translate_path}")
            target_lan = input_valid_language()
        print("Thanks for using GSpy!")
