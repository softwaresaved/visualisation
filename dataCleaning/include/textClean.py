#!/usr/bin/env python
# encoding: utf-8

"""
    Transforming any raw text into a bag of words.
    It gets a raw text composed of one sentence or an entire paragraph.
    From there it splits the text into list of sentence.
    Before splitting sentence into words it removes the emails and the
    URL addresses.
    Then it split every sentences into lists of words using regex and
    remove some noises
"""

import string
import re
import unicodedata
import sys

from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from include.textProcess import textProcess

# from include.benchmark import timeit
# from logger import logger
# logger = logger(name='textProcess', stream_level='INFO')


class textClean(textProcess):
    """
        Get a string as input of several sentence (or One), clean the text and return a list of words
        Break the text into several sentences
        Break the sentence into list of words
        Lower Case the words
        Remove stopwords, emails, URL, numbers, money symbol, punctuation, I
        Transform the 'll 's and remove them
        Flatten the list
        Return the list
    """

    def __init__(self, nltk_path=None):
        """
            Create the regex used later in the class.
        """
        textProcess.__init__(self, nltk_path)
        # self.txt_transform = txt_transform
        self.stop_words = stopwords.words('english')
        # Used to get all form of URL to remove them
        # http://stackoverflow.com/questions/14081050/remove-all-forms-of-urls-from-a-given-string-in-python
        self.REGEX_URL = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
        # Use to remove the trailing punctuation in words that remain after tokenization
        self.REGEX_EMAIL = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`" "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|" "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
        self.REGEX_SPLIT = re.compile(',|/|-|\s|\'')
        # To remove trailing space with translate in python 3, need to apply
        # the following workaround in order to build the self.TABLE to use in
        # the translate func()
        # Workaround cam be found on the following
        # # http://stackoverflow.com/questions/11066400/remove-punctuation-from-unicode-formatted-strings/21635971#21635971
        # Discussion about removing punctuation
        # # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        self.TABLE = dict.fromkeys(i for i in range(sys.maxunicode)
                                   if unicodedata.category(chr(i)).startswith('P'))
        # Remove the `#` form the dic to keep in in case of c#
        # FIXME Not having any impact yet because the word_tokenise is splitting c# in 'c', '#'
        del self.TABLE[35]

    def break_sentence(self, text):
        """
            Use nltk to tokenize sentences and return a list of sentences
        """
        return sent_tokenize(text)

    def remove_website(self, sentence):
        """
            Remove website address from the sentence
        """
        return re.sub(self.REGEX_URL, '', sentence)

    def remove_email(self, sentence):
        """
            Remove email address with the REGEX_EMAIL
        """
        return re.sub(self.REGEX_EMAIL, '', sentence)

    def break_word(self, sent):
        """
            Break sentence into list of word.
            Can use either the word_tokenise (preferred) or own
            simple splitting -- Also split words into several words when
            symbol in self.REGEX_SPLIT are encountered
        """
        return word_tokenize(re.sub(self.REGEX_SPLIT, ' ', sent))
        # return re.split(self.REGEX_SPLIT, sent)

    def remove_punctuation(self, word):
        """
            Remove punctuation
        """
        if word:
            if word not in string.punctuation:
                return word

    def remove_trailing_punctuation(self, word):
        """
            Get a list of words and remove the trailing punctuation on the words
        """
        if word:
            return word.translate(self.TABLE)

    def lower_case(self, word):
        """
            Return lowered words
        """
        try:
            return word.lower()
        except AttributeError:
            pass

    def remove_stop(self, word):
        """
            Remove the word if in stop word list
        """
        if word not in self.stop_words:
            return word

    def remove_number(self, word):
        """
            Remove all the numbers
        """
        def check_numeric(s):
            """ Check if a string is a numeric, Return True if yes
            """
            try:
                float(s)
                return True
            except (ValueError, TypeError):
                return False
        if check_numeric(word) is False:
            return word

    def transform_apostrophe(self, word):
        """
            After tokenise the `'ll` `'s` `'nt` are considered as single word
            - `'s`: Removed as it is kept like that later and not being
                    distinguished between the verb and the possessive
                    #  TODO Check if the pos_tag_sentence() makes accurate distinction
            - `'ll`: transform into `will`
            - `'nt`: Is transformed into `n't` by the token_sentence().
                     Convert this `n't` into `not`
        """
        if word:
            if word.startswith("'"):
                if word == "'s":
                    pass
                elif word == "'ll":
                    return 'will'
                else:
                    return word
            else:
                if word == "n't":
                    return 'not'
                else:
                    return word

    def remove_I(self, word):
        """ Remove the I that is not removed from the stop words list """
        if word != 'i':
            return word

    def remove_currency(self, word):
        """ Remove all the money symbol and the money associated if they are attached
        """
        # http://stackoverflow.com/questions/25978771/what-is-regex-for-currency-symbol
        if word:
            for ch in [word[0], word[-1]]:
                if unicodedata.category(ch) == 'Sc':
                    return None
            return word

    def remove_empty_words(self, word):
        """ Sometime empty words are kept in the sentence ['', 'word']
            probably due to break_word(). Need to fix that.
            Right now workaround to remove them before doing pos_tag
            Otherwise pos_tag throw an IndexError
        """
        if word != '':
            return word

    def flattening_list(self, text):
        """ Flattening the list of list into a flat list """
        return [word for sentence in text for word in sentence]

    def run(self, text):
        """ """
        txt_cleaned = list()
        # txt_transformed = list()
        for sent in self.break_sentence(text):
            sent = self.remove_website(sent)
            sent = self.remove_email(sent)
            sent_cleaned = list()
            # sent_transformed = list()
            for word in self.break_word(sent):
                word = self.transform_apostrophe(word)
                # word = self.remove_punctuation(word)
                word = self.remove_trailing_punctuation(word)
                word = self.remove_empty_words(word)
                word = self.remove_stop(word)
                word = self.remove_number(word)
                word = self.lower_case(word)
                word = self.remove_I(word)
                word = self.remove_currency(word)
                if word:
                    sent_cleaned.append(word)
            txt_cleaned.append(sent_cleaned)
            # if self.txt_transform is True:
            #     sent_transformed = self.pos_tag_sentence(sent_cleaned)
            #     sent_transformed = self.lem_word(sent_transformed)
            #     sent_transformed = self.stem_word(sent_transformed)
            # txt_transformed.append(sent_transformed)
        txt_cleaned = self.flattening_list(txt_cleaned)
        print(txt_cleaned)
        # txt_transformed = self.flattening_list(txt_transformed)
        # return txt_cleaned, txt_transformed
        return txt_cleaned


def main():
    # sentence = "A small test1  I you  will For the second's don't   take the asp.net because I need to program in c++ and in c# in R Each £ sentence £34234234, ala.group@somewhere.co.uk 321321312  http://www.group.com?yes , -12313 won't program in c# wouldn't I'll not pass the she doesn't his passes he's mentions' are perfect. exams's certificate, it's not my problem, as exam, test1. Second test"
    sentence = 'Petit test/pour voir-si/ca/fonction bien sans pour autant. Tout casserrrrr/.'
    print(sentence)
    process = textClean(txt_transform=False)
    cleaned = process.run(sentence)
    print(cleaned)
    # print(transformed)


if __name__ == '__main__':
    main()
