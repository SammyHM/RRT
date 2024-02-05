# pip install nltk
# https://www.turing.com/kb/5-powerful-text-summarization-techniques-in-python
from nltk.corpus import stopwords                       
from nltk.tokenize import word_tokenize, sent_tokenize

# pip install translate
from translate import Translator


class NaturalLanguange:


    dictionaries = {
        "afrikaans"     :   "af",
        "albanian"	    :   "sq",
        "amharic"	    :   "am",
        "arabic"	    :   "ar",
        "armenian"	    :   "hy",
        "assamese"	    :   "as",
        "aymara"	    :   "ay",
        "azerbaijani"	:   "az",
        "bambara"	    :   "bm",
        "basque"	    :   "eu",
        "belarusian"	:   "be",
        "bengali"	    :   "bn",
        "bhojpuri"	    :   "bho",
        "bosnian"	    :   "bs",
        "bulgarian"	    :   "bg",
        "catalan"	    :   "ca",
        "cebuano"	    :   "ceb",
        "chinese"       :   "zh",
        "corsican"	    :   "co",
        "croatian"	    :   "hr",
        "czech"	        :   "cs",
        "danish"	    :   "da",
        "dhivehi"	    :   "dv",
        "dogri"	        :   "doi",
        "dutch"	        :   "nl",
        "english"	    :   "en",
        "esperanto"	    :   "eo",
        "estonian"	    :   "et",
        "ewe"	        :   "ee",
        "filipino"      :   "fil",
        "finnish"	    :   "fi",
        "french"	    :   "fr",
        "frisian"	    :   "fy",
        "galician"	    :   "gl",
        "georgian"	    :   "ka",
        "german"	    :   "de",
        "greek"	        :   "el",
        "guarani"	    :   "gn",
        "gujarati"	    :   "gu",
        "haitian"       :   "ht",
        "hausa"	        :   "ha",
        "hawaiian"	    :   "haw",
        "hebrew"	    :   "he",
        "hindi"	        :   "hi",
        "hmong"	        :   "hmn",
        "hungarian"	    :   "hu",
        "icelandic"	    :   "is",
        "igbo"	        :   "ig",
        "ilocano"	    :   "ilo",
        "indonesian"	:   "id",
        "irish"	        :   "ga",
        "italian"	    :   "it",
        "japanese"	    :   "ja",
        "javanese"	    :   "jv",
        "kannada"	    :   "kn",
        "kazakh"	    :   "kk",
        "khmer"	        :   "km",
        "kinyarwanda"	:   "rw",
        "konkani"	    :   "gom",
        "korean"	    :   "ko",
        "krio"	        :   "kri",
        "kurdish"	    :   "ku",
        "kyrgyz"	    :   "ky",
        "lao"	        :   "lo",
        "latin"	        :   "la",
        "latvian"	    :   "lv",
        "lingala"	    :   "ln",
        "lithuanian"	:   "lt",
        "luganda"	    :   "lg",
        "luxembourgish"	:   "lb",
        "macedonian"	:   "mk",
        "maithili"	    :   "mai",
        "malagasy"	    :   "mg",
        "malay"	        :   "ms",
        "malayalam"	    :   "ml",
        "maltese"	    :   "mt",
        "maori"	        :   "mi",
        "marathi"	    :   "mr",
        "mizo"	        :   "lus",
        "mongolian"	    :   "mn",
        "myanmar"       :   "my",
        "nepali"	    :   "ne",
        "norwegian"	    :   "no",
        "nyanja"        :   "ny",
        "odia"          :   "or",
        "oromo"	        :   "om",
        "pashto"	    :   "ps",
        "persian"	    :   "fa",
        "polish"	    :   "pl",
        "portuguese"    :   "pt",
        "punjabi"	    :   "pa",
        "quechua"	    :   "qu",
        "romanian"	    :   "ro",
        "russian"	    :   "ru",
        "samoan"	    :   "sm",
        "sanskrit"	    :   "sa",
        "scots Gaelic"	:   "gd",
        "sepedi"	    :   "nso",
        "serbian"	    :   "sr",
        "sesotho"	    :   "st",
        "shona"	        :   "sn",
        "sindhi"	    :   "sd",
        "sinhala"       :   "si",
        "slovak"	    :   "sk",
        "slovenian"	    :   "sl",
        "somali"	    :   "so",
        "spanish"	    :   "es",
        "sundanese"	    :   "su",
        "swahili"	    :   "sw",
        "swedish"	    :   "sv",
        "tagalog"       :   "tl",
        "tajik"	        :   "tg",
        "tamil"	        :   "ta",
        "tatar"	        :   "tt",
        "telugu"	    :   "te",
        "thai"	        :   "th",
        "tigrinya"      :   "ti",
        "tsonga"	    :   "ts",
        "turkish"	    :   "tr",
        "turkmen"	    :   "tk",
        "twi"         	:   "ak",
        "ukrainian"	    :   "uk",
        "urdu"	        :   "ur",
        "uyghur"	    :   "ug",
        "uzbek"	        :   "uz",
        "vietnamese"	:   "vi",
        "welsh"	        :   "cy",
        "xhosa"	        :   "xh",
        "yiddish"	    :   "yi",
        "yoruba"	    :   "yo",
        "zulu"	        :   "zu"
    }


    def __init__(self, language: str):
        self.stopwords = language

    
    def text_reduction(self, text: str, deviations = 1.7) -> str:
        """ Reduces text by calculating a score for each sentece, it's mean
            and as a result, return all senteces that deviate positively from it.
        """
        # Set word frequency
        words = word_tokenize(text)
        word_frequency = {}
        for word in words:
            word = word.lower()
            if word in self.stopwords:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
        # Set sentence score, based on word frequency
        sentences = sent_tokenize(text)
        sentence_score = {}
        for sentence in sentences:
            for word, frequency in word_frequency.items():
                if word in sentence.lower():
                    if sentence in sentence_score:
                        sentence_score[sentence] += frequency
                    else:
                        sentence_score[sentence] = 1
        # Average sentence value
        mean_score = 0
        for sentence in sentence_score:
            mean_score += sentence_score[sentence]
        mean_score /= len(sentence_score)
        # Append valuable sentences, those that have a certain deviation from the mean
        summary = ''
        for sentence in sentences:
            if sentence in sentence_score and sentence_score[sentence] > deviations * mean_score:
                summary += sentence + "\n"
        # Check if any valuable sentece was found, otherwise show just one sentece
        return summary if summary != '' else max(sentence_score)


    @staticmethod
    def translate(text: str, to_lang: str):
        """ Given a target language, translates
        """
        NaturalLanguange.assert_valid_language(to_lang)

        to_lang = NaturalLanguange.dictionaries[to_lang]
        from_lan = "autodetect"
        translator = Translator(to_lang=to_lang, from_lan=from_lan)

        translation = ""
        sentences = sent_tokenize(text)
        try:
            for sentence in sentences:
                translation += translator.translate(sentence) + " "
        except Exception as error:
            translation = "Translation unavailable, try in a day's time."
        return translation


    @staticmethod
    def is_valid_language(language: str) -> bool:
        return language in list(NaturalLanguange.dictionaries.keys())


    @staticmethod
    def assert_valid_language(language: str):
        if not NaturalLanguange.is_valid_language(language):
            raise Exception(f"Invalid language: {language}")
        

    @property
    def stopwords(self) -> set():
        return self._stopwords


    @stopwords.setter
    def stopwords(self, language: str):
        self.assert_valid_language(language)
        self._stopwords = set(stopwords.words(language))
