#!/bin/bash

usage() {
    echo "Usage: $0 [--setup]"
}

case "$1" in 
    --setup)
        virtualenv venv -p /usr/local/bin/python3
        source ./venv/bin/activate
        pip install -r requirements.txt
        mkdir ./venv/nltk_data
        python -m nltk.downloader -d ./venv/nltk_data mac_morpho 
        python -m nltk.downloader -d ./venv/nltk_data floresta
        deactivate
        ;;
    --run)
        docker run -it kb
        ;;
    *)
        usage
        ;;
esac
