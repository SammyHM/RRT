# Natural Language

<table>
  <tr>
    <td>
      <div style="font-weight: bold;">def text_reduction(self, text: str, deviations = 1.8) &rarr; str:</div>
      <div style="font-style: italic;">Reduces text by calculating a score for each sentece, it's mean and as a result, return all senteces that deviate positively from it.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def translate(self, text: str, to_lang: str): &rarr; str:</div>
      <div style="font-style: italic;">Given a target language, returns a translation of the given text. <br> Throws Exception if to_lang is not deinfed as a valid language.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">@staticmethod <br> def is_valid_language(language: str) &rarr; bool:</div>
      <div style="font-style: italic;">Returns True/False if language is registered in the NaturalLanguage dictionary.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">@staticmethod <br> def assert_valid_language(language: str): &rarr; None:</div>
      <div style="font-style: italic;">Raises an exeption if language is not registered in the NatrualLanguage dictionary.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">@property <br> def stopwords(self) &rarr; set():</div>
      <div style="font-style: italic;">Defines a list of valid words for a language.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">@stopwords.setter <br> def stopwords(self, language: str): &rarr; None:</div>
      <div style="font-style: italic;">Sets stopwords properties for a valid language.</div>
    </td>
  </tr>
</table>

# Bibliografía

* [Natural Language Tool Kit.](https://www.kaggle.com/code/imkrkannan/text-summarization-with-nltk-in-python)