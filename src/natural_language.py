from nltk.corpus import stopwords                       
from nltk.tokenize import word_tokenize, sent_tokenize
from numpy import mean, std

from translate import Translator


class NaturalLanguange:


    dictionaries = {
        "albanian"	    :   "sq",
        "arabic"	    :   "ar",
        "azerbaijani"	:   "az",
        "bengali"	    :   "bn",
        "bulgarian"	    :   "bg",
        "catalan"	    :   "ca",
        "cebuano"	    :   "ceb",
        "chinese"       :   "zh",
        "chinese-t"     :   "zt",
        "czech"	        :   "cs",
        "danish"	    :   "da",
        "dutch"	        :   "nl",
        "english"	    :   "en",
        "esperanto"	    :   "eo",
        "estonian"	    :   "et",
        "finnish"	    :   "fi",
        "french"	    :   "fr",
        "german"	    :   "de",
        "greek"	        :   "el",
        "hebrew"	    :   "he",
        "hindi"	        :   "hi",
        "hungarian"	    :   "hu",
        "indonesian"	:   "id",
        "irish"	        :   "ga",
        "italian"	    :   "it",
        "japanese"	    :   "ja",
        "korean"	    :   "ko",
        "latvian"	    :   "lv",
        "lithuanian"	:   "lt",
        "malay"	        :   "ms",
        "norwegian"	    :   "no",
        "persian"	    :   "fa",
        "polish"	    :   "pl",
        "portuguese"    :   "pt",
        "romanian"	    :   "ro",
        "russian"	    :   "ru",
        "serbian"	    :   "sr",
        "slovak"	    :   "sk",
        "slovenian"	    :   "sl",
        "spanish"	    :   "es",
        "swedish"	    :   "sv",
        "tagalog"       :   "tl",
        "thai"	        :   "th",
        "turkish"	    :   "tr",
        "ukrainian"	    :   "uk",
        "urdu"	        :   "ur",
        "vietnamese"	:   "vi",
    }


    def __init__(self, language: str):
        self.stopwords = language

    
    def text_reduction(self, text: str, deviations = 1.5) -> str:
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
        # Set minimum value for score to be important
        scores = list(sentence_score.values())
        score_mean = mean(scores)
        score_std = std(scores)
        importance_limit = score_mean + deviations * score_std
        # Append valuable sentences, those that have a certain deviation from the mean
        summary = ''
        for sentence in sentences:
            if sentence in sentence_score and sentence_score[sentence] > importance_limit:
                summary += sentence + "\n"
        # Check if any valuable sentece was found, otherwise show just one sentece
        return summary if summary != '' else max(sentence_score)


    def translate(self, text: str, to_lang: str) -> str:
        """ Given a target language, returns a translation of the given text.
            Throws Exception if to_lang is not deinfed as a valid language.
        """
        # Validate input
        NaturalLanguange.assert_valid_language(to_lang)
        # Setup translator
        to_lang = NaturalLanguange.dictionaries[to_lang]
        translator = Translator(from_lang='autodetect', to_lang=to_lang)
        # Translate sentence by sentence
        translation = ""
        sentences = sent_tokenize(text)
        for sentence in sentences:
            if len(sentence) < 500:
                translation += translator.translate(sentence) + " "
        return translation


    @staticmethod
    def is_valid_language(language: str) -> bool:
        """ Returns True/False if language is registered in the NaturalLanguage dictionary.
        """
        return language in list(NaturalLanguange.dictionaries.keys())


    @staticmethod
    def assert_valid_language(language: str) -> None:
        """ Raises an exeption if language is not registered in the NatrualLanguage dictionary.
        """
        if not NaturalLanguange.is_valid_language(language):
            raise Exception(f"Invalid language: {language}")
        

    @property
    def stopwords(self) -> set():
        """ Defines a list of valid words for a language.
        """
        return self._stopwords


    @stopwords.setter
    def stopwords(self, language: str) -> None:
        """ Sets stopwords properties for a valid language.
        """
        self.assert_valid_language(language)
        self._stopwords = set(stopwords.words(language))
