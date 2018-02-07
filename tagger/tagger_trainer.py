# encoding: utf-8

import os
from pickle import dump
import nltk
from nltk.corpus import floresta, mac_morpho
from tagger.tagger_base import TaggerBase
from tagger.corpus import Corpus

class TaggerTrainer(TaggerBase):
    def exists(self, corpus_name, tagger_name):
        path = self.build_path(corpus_name, tagger_name)
        return os.path.isfile(path)

    def save_tagger(self, tagger, corpus_name, tagger_name):
        path = self.build_path(corpus_name, tagger_name)
        output = open(path, "wb")
        dump(tagger, output, -1)
        output.close()

    def build_tagger(self, corpus_name, train_sents, tagger_name, tagger_class, backoff):
        if not self.exists(corpus_name, tagger_name) or self.should_force:
            tagger = tagger_class(train_sents, backoff=backoff)
            self.save_tagger(tagger, corpus_name, tagger_name)

    def train(self, corpus_name, train_sents):
        print("Default tagger")
        default_tagger = nltk.DefaultTagger('NN')

        print("Train Unigram")
        unigram_tagger = self.build_tagger(
            corpus_name, train_sents, "unigram", nltk.UnigramTagger, default_tagger)

        print("Train Bigram")
        bigram_tagger = self.build_tagger(
            corpus_name, train_sents, "bigram", nltk.BigramTagger, unigram_tagger)

        print("Train Trigram")
        self.build_tagger(
            corpus_name, train_sents, "trigram", nltk.TrigramTagger, bigram_tagger)

    def run(self, corpus=Corpus.FLORESTA, force=False):
        self.should_force = force

        if corpus == Corpus.FLORESTA:
            print("\n##### Floresta Corpus #####")
            floresta_sent = floresta.tagged_sents()
            self.train("floresta", floresta_sent)
        elif corpus == Corpus.MAC_MORPHO:
            print("\n###### Mac Morpho Corpus #####")
            mac_morpho_sent = mac_morpho.tagged_sents()
            self.train("mac_morpho", mac_morpho_sent)
