#### How to Demo

1. Launch your Message Queue Server a Project Root
```
# 建議 work 會去執行 Python 程式必須再跟你 *.py 同一層目錄否則執行會找不到 job_function_collection.py 檔案
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
