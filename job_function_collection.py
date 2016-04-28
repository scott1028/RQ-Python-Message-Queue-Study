# coding: utf-8

import time
import requests

# Your Main Job Function Logic
def count_words_at_url(url):
    """Just an example function that's called async."""
    print 'start at:', time.time()
    resp = requests.get(url)
    time.sleep(2)  # mock a job timeout
    print 'end at:', time.time()
    return len(resp.text.split())

