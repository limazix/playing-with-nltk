# encoding: utf-8

import os
from pickle import dump, load
import nltk
from nltk.corpus import floresta, mac_morpho
# from nltk.tokenize import word_tokenize


class Tagger:

    def build_path(self, corpus_name, tagger_name):
        venv = os.getcwd() + "/venv"
        return venv + "/taggers/" + corpus_name + "_" + tagger_name + ".pkl"

    def if_exists(self, corpus_name, tagger_name):
        path = self.build_path(corpus_name, tagger_name)
        return os.path.isfile(path)

    def save_tagger(self, tagger, corpus_name, tagger_name):
        path = self.build_path(corpus_name, tagger_name)
        output = open(path, "wb")
        dump(tagger, output, -1)
        output.close()

    def get_tagger(self, corpus_name, train_sents, tagger_name, tagger_class, backoff):
        if self.if_exists(corpus_name, tagger_name):
            path = self.build_path(corpus_name, tagger_name)
            data = open(path, "rb")
            tagger = load(data)
            data.close()
            return tagger
        else:
            tagger = tagger_class(train_sents, backoff=backoff)
            self.save_tagger(tagger, corpus_name, tagger_name)
            return tagger

    def train(self, corpus_name, train_sents):
        print("Default tagger")
        default_tagger = nltk.DefaultTagger('NN')

        print("Train Unigram")
        unigram_tagger = self.get_tagger(
            corpus_name, train_sents, "unigram", nltk.UnigramTagger, default_tagger)

        print("Train Bigram")
        bigram_tagger = self.get_tagger(
            corpus_name, train_sents, "bigram", nltk.BigramTagger, unigram_tagger)

        print("Train Trigram")
        trigram_tagger = self.get_tagger(
            corpus_name, train_sents, "trigram", nltk.TrigramTagger, bigram_tagger)

        return trigram_tagger

    def run_tagger(self, corpus_name, tagger, tokenized):
        tagged_sent = tagger.tagged_sents()
        tagger_trained = self.train(corpus_name, tagged_sent)
        return tagger_trained.tag(tokenized)

    def run(self, text):
        tokenized = text.split() # word_tokenize(text)

        print("\n##### Floresta Corpus #####")
        floresta_result = self.run_tagger("floresta", floresta, tokenized)

        print("\n###### Mac Morpho Corpus #####")
        mac_morpho_result = self.run_tagger(
            "mac_morpho", mac_morpho, tokenized)

        print("Tagger result")
        result = {"floresta": floresta_result, "mac morpho": mac_morpho_result}

        return result
