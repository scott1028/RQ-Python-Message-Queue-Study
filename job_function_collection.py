# coding: utf-8

import requests

# Your Main Job Function Logic
def count_words_at_url(url):
    """Just an example function that's called async."""
    resp = requests.get(url)
    return len(resp.text.split())

