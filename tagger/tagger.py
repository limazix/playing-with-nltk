# encoding: utf-8

import os
from pickle import load
from nltk.tokenize import word_tokenize
from tagger.corpus import Corpus
from tagger.tagger_base import TaggerBase

class Tagger(TaggerBase):
    def get_tagger(self, corpus_name, tagger_name):
        path = self.build_path(corpus_name, tagger_name)
        data = open(path, "rb")
        tagger = load(data)
        data.close()
        return tagger

    def run_tagger(self, corpus_name, tokenized):
        tagger_trained = self.get_tagger(corpus_name, "trigram")
        return tagger_trained.tag(tokenized)

    def run(self, text, corpus=Corpus.FLORESTA):
        tokenized = word_tokenize(text, language='portuguese')

        if corpus == Corpus.FLORESTA:
            print("\n##### Floresta Corpus #####")
            return self.run_tagger("floresta", tokenized)
        elif corpus == Corpus.MAC_MORPHO:
            print("\n###### Mac Morpho Corpus #####")
            return self.run_tagger("mac_morpho", tokenized)
