from recommendation import search_pubs, best_publication, fetch_pdf_data, parse_pdf_data
from natural_language import NaturalLanguange
from data import create_txt, save_pubs, save_summaries


def input_valid_language() -> str:
    """ Prompt user to input a language, and returns it once a valid language was selected.
        User can also type quit.
    """
    print('Type "quit" to exit translation process.')
    language = input("Select a valid language: ").lower()
    while(language != 'quit' and not NaturalLanguange.is_valid_language(language)):
        language = input(f"There's no support for {language}. Select a valid Language: ").lower()
    return language


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
            translated_text = nl.translate(summary, target_lan)
            translate_path = create_txt(translated_text, article_name, target_lan)
            summary_data[target_lan] = translated_text
            print(f"Saved translation at: {translate_path}")
            target_lan = input_valid_language()
        # 4.- Save all summaries
        save_summaries(summary_data, query)
        print("Thanks for using GSpy!")
