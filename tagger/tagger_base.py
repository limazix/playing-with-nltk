# encoding: utf-8

import os

class TaggerBase:
    def build_path(self, corpus_name, tagger_name):
        venv = os.getcwd() + "/" + os.getenv('TAGGER_DATA', "venv")
        return venv + "/tagger_data/" + corpus_name + "_" + tagger_name + ".pkl"
