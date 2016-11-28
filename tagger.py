# encoding: utf-8

import nltk
from nltk.corpus import floresta, mac_morpho
from nltk.tokenize import word_tokenize
from pickle import dump, load

class Tagger:
    def if_exists(self, corpus_name, name): 
        return False

    def save_tagger(self, tagger, corpus_name, tagger_name):
        output = open("./taggers/" + corpus_name + "_" + tagger_name + ".pkl", "wb")
        dump(tagger, output, -1)
        output.close()

    def get_tagger(self, corpus_name, train_sents, tagger_name, tagger_class, backoff):
        if(self.if_exists(corpus_name, tagger_name)):
            input = open("./taggers/" + corpus_name + "_" + tagger_name + ".pkl", "rb")
            tagger = load(input)
            input.close()
        else:
            tagger = tagger_class(train_sents, backoff=backoff)
            self.save_tagger(tagger, corpus_name, tagger_name)
            return tagger

    def train(self, corpus_name, train_sents):
        print "Default tagger"
        default_tagger = nltk.DefaultTagger('NN')

        print "Train Unigram"
        unigram_tagger = self.get_tagger(corpus_name, train_sents, "unigram", nltk.UnigramTagger, default_tagger)

        print "Train Bigram"
        bigram_tagger = self.get_tagger(corpus_name, train_sents, "bigram", nltk.BigramTagger, unigram_tagger)

        print "Train Trigram"
        trigram_tagger = self.get_tagger(corpus_name, train_sents, "trigram", nltk.TrigramTagger, bigram_tagger)

        return trigram_tagger

    def run_tagger(self, corpus_name, tagger, tokenized):
        tagged_sent = tagger.tagged_sents()
        tagger_trained = self.train(corpus_name, tagged_sent)
        return tagger_trained.tag(tokenized)

    def run(self, text):
        tokenized = word_tokenize(text)

        print "\n##### Floresta Corpus #####"
        floresta_result = self.run_tagger("floresta", floresta, tokenized)

        print "\n###### Mac Morpho Corpus #####"
        mac_morpho_result = self.run_tagger("mac_morpho", mac_morpho, tokenized)

        result = {"floresta": floresta_result, "mac morpho": mac_morpho_result}
        
        return result
