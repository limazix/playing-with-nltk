# encoding: utf-8

import logging
import json
import os
from tagger import Tagger, TaggerTrainer

from flask import Flask, request
app = Flask(__name__)

PORT = int(os.getenv('PORT', 8000))

@app.route("/")
def hello():
    return "Playing with NLTK"

@app.route("/api/pos", methods=["POST"])
def pos():
    post_data = request.json["text"]

    text_tagger = Tagger()
    response = text_tagger.run(post_data)

    return json.dumps(response)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    TaggerTrainer().run()
    app.run(host='0.0.0.0', port=PORT, debug=True)
