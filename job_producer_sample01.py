# coding: utf-8

from redis import Redis
from rq import Queue

# q = Queue(connection=Redis('127.0.0.1', 6379))
q = Queue(connection=Redis())

from job_function_collection import count_words_at_url
result_fd = q.enqueue(count_words_at_url, 'http://nvie.com')

# import pdb; pdb.set_trace()

print result_fd.result

import time
time.sleep(2)
print result_fd.result
