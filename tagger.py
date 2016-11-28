# encoding: utf-8

import nltk
from nltk.corpus import floresta, mac_morpho
from nltk.tokenize import word_tokenize

def train(train_sents):
    print "Default tagger"
    t0 = nltk.DefaultTagger('NN')
    print "Train Unigram"
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    print "Train Bigram"
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    print "Train Trigram"
    t3 = nltk.TrigramTagger(train_sents, backoff=t2)
    return t3

def run_tagger(tagger, tokenized):
    tagged_sent = tagger.tagged_sents()
    tagger_trained = train(tagged_sent)
    print tagger_trained.tag(tokenized)
    #print tagger_trained.evaluate(tokenized)


text = """Estou testando o NLTK para português brasiileiro."""
tokenized = word_tokenize(text)

print "\n##### Floresta Corpus #####"
run_tagger(floresta, tokenized)

print "\n###### Mac Morpho Corpus #####"
run_tagger(mac_morpho, tokenized)
