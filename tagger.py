# encoding: utf-8

import nltk
from nltk.corpus import floresta, mac_morpho
from nltk.tokenize import word_tokenize

class Tagger:
    def train(self, train_sents):
        print "Default tagger"
        t0 = nltk.DefaultTagger('NN')
        print "Train Unigram"
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        print "Train Bigram"
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        print "Train Trigram"
        t3 = nltk.TrigramTagger(train_sents, backoff=t2)
        return t3

    def run_tagger(self, tagger, tokenized):
        tagged_sent = tagger.tagged_sents()
        tagger_trained = self.train(tagged_sent)
        #print tagger_trained.tag(tokenized)
        #print tagger_trained.evaluate(tokenized)
        return tagger_trained.tag(tokenized)

    def run(self, text):
        tokenized = word_tokenize(text)

        print "\n##### Floresta Corpus #####"
        floresta_result = self.run_tagger(floresta, tokenized)

        print "\n###### Mac Morpho Corpus #####"
        mac_morpho_result = self.run_tagger(mac_morpho, tokenized)

        return {"floresta": floresta_result, "mac morpho": mac_morpho_result}
