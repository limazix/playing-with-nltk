# encoding: utf-8

import os
from pickle import load
from nltk.tokenize import word_tokenize

class Tagger:
    def build_path(self, corpus_name, tagger_name):
        venv = os.getcwd() + "/venv"
        return venv + "/taggers/" + corpus_name + "_" + tagger_name + ".pkl"

    def get_tagger(self, corpus_name, tagger_name):
        path = self.build_path(corpus_name, tagger_name)
        data = open(path, "rb")
        tagger = load(data)
        data.close()
        return tagger

    def run_tagger(self, corpus_name, tokenized):
        tagger_trained = self.get_tagger(corpus_name, "trigram")
        return tagger_trained.tag(tokenized)

    def run(self, text):
        tokenized = word_tokenize(text, language='portuguese')

        print("\n##### Floresta Corpus #####")
        floresta_result = self.run_tagger("floresta", tokenized)

        print("\n###### Mac Morpho Corpus #####")
        mac_morpho_result = self.run_tagger(
            "mac_morpho", tokenized)

        print("Tagger result")
        result = {"floresta": floresta_result, "mac morpho": mac_morpho_result}

        return result
