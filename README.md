#### How to Demo

0. List Status
```
rq --help
Commands:
  empty    Empty given queues.
  info     RQ command-line monitor.
  requeue  Requeue failed jobs.
  resume   Resumes processing of queues, that where...
  suspend  Suspends all workers, to resume run `rq...
  worker   Starts an RQ worker.
rq info
```

1. Launch your Message Queue Server a Project Root
```
# 建議 work 會去執行 Python 程式必須再跟你 *.py 同一層目錄否則執行會找不到 job_function_collection.py 檔案
# 你可以啟動很多个 Worker 他們會分擔 Queue 內的工作！
rq worker
rq worker
rq worker
	...
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
