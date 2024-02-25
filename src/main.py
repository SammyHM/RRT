from recommendation import search_pubs, best_publication, get_publication_name, get_publication_url, get_publication_abstract, fetch_pdf_data
from natural_language import NaturalLanguange
from data import create_txt, save_pubs, save_summaries, write_pdf_data, parse_pdf_data
from re import sub as replace


def input_valid_language() -> str:
    """ Prompt user to input a language, and returns it once a valid language was selected.
        User can also type quit.
    """
    print('Type "quit" to exit translation process.')
    language = input("Select a valid language: ").lower()
    while(language != 'quit' and not NaturalLanguange.is_valid_language(language)):
        language = input(f"There's no support for {language}. Select a valid Language: ").lower()
    return language


def valid_text_file(name: str) -> str:
    """ Given a string, returns a string which is valid for file naming.
    """
    return replace(r'[<>:"/\\|?*]', ' ', name)


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
        print(f"Best article found is: '{get_publication_name(best)}'.")
        print(f"Link: {get_publication_url(best)}.")
        print("Fetching data...")
        pdf_data = fetch_pdf_data(best)
        if pdf_data == None:
            print("Fetching the article data is unavailable at the moment. Try in two days time.")
        else:
            print("Parsing data...")
            article_name = valid_text_file(query)
            write_pdf_data(article_name, pdf_data)
            text = parse_pdf_data(article_name)
            # 2.- Summerize text
            print(f"\nSummarizing its contents...")
            summary = f"Abstract:\n{get_publication_abstract(best)}\n\nContent:\n{nl.text_reduction(text)}"
            summary_path = create_txt(summary, article_name)
            print(f'Saved summary at {summary_path}')
            summary_data = {'default': summary}
            # 3.- Translate summary
            print(f'\nAvailable languages: {NaturalLanguange.dictionaries.keys()}')
            target_lan = input_valid_language()
            while target_lan.lower() != 'quit':
                print(f"Translating document to {target_lan}...")
                translated_text = nl.translate(summary, target_lan)
                translate_path = create_txt(translated_text, article_name, target_lan)
                summary_data[target_lan] = translated_text
                print(f"Saved translation at: {translate_path}")
                target_lan = input_valid_language()
            # 4.- Save all summaries
            save_summaries(summary_data, query)
            print("Thanks for using GSpy!")
