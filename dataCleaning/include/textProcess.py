#!/usr/bin/env python
# encoding: utf-8

"""
   Receive a string input and transform it with the NLTK library
   1. Tag the words with a POS_TAG
   2. Apply a stemmer
   3. Return a list of stemmed words
"""


from nltk import pos_tag, data
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# from include.benchmark import timeit
# from logger import logger
# logger = logger(name='textProcess', stream_level='INFO')


class textProcess(object):
    """ """
    def __init__(self, nltk_path=None):
        """
            Init the stop word list, stemmer and lemmatizer from the nltk library
        """
        # Add the path to the nltk module to search the files within that folder
        # Allow to install the nltk files directly in the current folder
        self.nltk_path = nltk_path
        if self.nltk_path:
            data.path.append(nltk_path)
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def pos_tag_sentence(self, sentence):
        """
            Get a sentence as a list and return a list of tuple with the
            information on the word. Used for the stemmization later
        """
        return pos_tag(sentence)

    def lem_word(self, sentence):
        """
            Get a tuple of word and lemmize word
        """
        def convert_tag(tag):
            """
                Need to convert the POS_TAG into the recognized form for the
                lemmatizer
            """
            if tag.startswith('J'):
                return wordnet.ADJ
            elif tag.startswith('V'):
                return wordnet.VERB
            elif tag.startswith('N'):
                return wordnet.NOUN
            elif tag.startswith('R'):
                return wordnet.ADV
            elif tag.startswith('s'):
                return wordnet.ADJ_SAT
            else:
                return None

        list_file = list()
        for word in sentence:
            pos_tag = convert_tag(word[1])
            if pos_tag:
                lem = self.lemmatizer.lemmatize(word[0], pos=pos_tag)
            else:
                lem = self.lemmatizer.lemmatize(word[0])
            list_file.append(lem)
        return list_file

    def stem_word(self, sentence):
        """
            Stemming is the process of reducing a word into its root form.
            The root form is not necessarily a word by itself, but it can be
            used to generate words by concatenating the right suffix.
            source: http://marcobonzanini.com/2015/01/26/stemming-lemmatisation-and-pos-tagging-with-python-and-nltk/
        """
        return [self.stemmer.stem(word) for word in sentence]

    def run(self, txt):
        """ Run method to get a text str and return the full transformed
            string back
            Parameters:
            * txt: list of string
            Return:
            * transformed_txt: list of string (transformed with the method
                               from the classe()
        """
        txt = self.pos_tag_sentence(txt)
        txt = self.lem_word(txt)
        txt = self.stem_word(txt)
        return txt


def main():
    pass

if __name__ == '__main__':
    main()
