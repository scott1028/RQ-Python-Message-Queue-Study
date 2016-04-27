#### How to Demo

1. Launch your Message Queue Server a Project Root
```
rq worker
```

2. Open Your Python Interactive Shell or execute job_producer_sample01.py

```
# coding: utf-8

from redis import Redis
from rq import Queue

# 建立 Queue 使用 Redis
q = Queue(connection=Redis())

from job_function_collection import count_words_at_url

# 把 "執行 Function 的 Job" 推送到 Message Queue 執行
result_fd = q.enqueue(count_words_at_url, 'http://nvie.com')

# 當下不會有結果因為是 Async 的
print result_fd.result

import time
time.sleep(1)

# 等個幾秒可以得到正確結果
print result_fd.result
```
