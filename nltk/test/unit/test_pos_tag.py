# -*- coding: utf-8 -*-
"""
Tests for BLEU translation evaluation metric
"""

import unittest

from nltk.tag import word_tokenize, pos_tag

    >>> from nltk import pos_tag, word_tokenize
    >>> pos_tag(word_tokenize("John's big idea isn't all that bad."))
    [('John', 'NNP'), ("'s", 'POS'), ('big', 'JJ'), ('idea', 'NN'), ('is', 'VBZ'),
    ("n't", 'RB'), ('all', 'PDT'), ('that', 'DT'), ('bad', 'JJ'), ('.', '.')]

A Russian tagger is also available if you specify lang="rus". It uses
the Russian National Corpus tagset:

    >>> pos_tag(word_tokenize("Илья оторопел и дважды перечитал бумажку."), lang='rus')



class TestPosTag(unittest.TestCase):
    def test_pos_tag_eng(self):
        text = "John's big idea isn't all that bad."
        expected_tagged = [('John', 'NNP'), ("'s", 'POS'), ('big', 'JJ'),
                           ('idea', 'NN'), ('is', 'VBZ'), ("n't", 'RB'),
                           ('all', 'PDT'), ('that', 'DT'), ('bad', 'JJ'),
                           ('.', '.')]
        assert pos_tag(word_tokenize(text)) == expected_tagged

    def test_pos_tag_eng_universal(self):
        text = "John's big idea isn't all that bad."
        expected_tagged = [('John', 'NOUN'), ("'s", 'PRT'), ('big', 'ADJ'),
                           ('idea', 'NOUN'), ('is', 'VERB'), ("n't", 'ADV'),
                           ('all', 'DET'), ('that', 'DET'), ('bad', 'ADJ'),
                           ('.', '.')]
        assert pos_tag(word_tokenize(text), tagset='universal') == expected_tagged

    def test_pos_tag_rus(self):
        text = u"Илья оторопел и дважды перечитал бумажку."
        expected_tagged = [('Илья', 'S'), ('оторопел', 'V'), ('и', 'CONJ'),
                           ('дважды', 'ADV'), ('перечитал', 'V'),
                           ('бумажку', 'S'), ('.', 'NONLEX')]
        assert pos_tag(word_tokenize(text), lang='rus') == expected_tagged

    def test_pos_tag_rus(self):
        text = u"Илья оторопел и дважды перечитал бумажку."
        expected_tagged = [('Илья', 'NOUN'), ('оторопел', 'VERB'),
                           ('и', 'SCONJ'), ('дважды', 'ADV'),
                           ('перечитал', 'VERB'), ('бумажку', 'NOUN'),
                           ('.', 'X')]
        assert pos_tag(word_tokenize(text),  tagset='universal', lang='rus') == expected_tagged
