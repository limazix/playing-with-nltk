#!/bin/bash

usage() {
    echo "Usage: $0 [--setup]"
}

case "$1" in 
    --setup)
        virtualenv venv -p /usr/local/bin/python3
        source ./venv/bin/activate
        pip install -r requirements.txt
        mkdir ./venv/taggers
        mkdir ./venv/nltk_data
        python -m nltk.downloader mac_morpho
        python -m nltk.downloader floresta
        python -m nltk.downloader punkt
        deactivate
        ;;
    --run)
        source ./venv/bin/activate
        python server.py
        deactivate
        ;;
    *)
        usage
        ;;
esac
