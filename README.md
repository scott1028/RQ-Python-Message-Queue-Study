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

1. Launch your Message Queue Server a Project Root(你也可以事後在啟動，他就是抓 Redis 內的 Job 逐步執行而已。)
```
# 建議 work 會去執行 Python 程式必須再跟你 *.py 同一層目錄否則執行會找不到 job_function_collection.py 檔案
# 你可以啟動很多个 Worker 他們會分擔 Queue 內的工作！
# 預設連線 Redis localhost:6379！
rq worker
rq worker
rq worker
rq worker -c settings
	...
```

2. Open Your Python Interactive Shell or execute job_producer_sample01.py

```
# coding: utf-8

from redis import Redis
from rq import Queue

# 建立 Queue 使用 Redis
# Job Producer 的 Redis 與 Job Comsumer 的 Redis 可以設定為不同的。但是一般人不會這樣做！
# q = Queue(connection=Redis('127.0.0.1', 6379))
q = Queue(connection=Redis('127.0.0.1', 6379, '1'))  # index of redis
# q = Queue(connection=Redis())

# 即使 Job Comsumer(qr worker) 目前沒有啟動也不會出錯，本 Job Client 會將 Job 先推送到 Redis 等 worker 啟動後就會逐步執行了！
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

#### Others

- ref: https://pypi.python.org/pypi/redis

![Alt text](https://raw.githubusercontent.com/scott1028/RQ-Python-Message-Queue-Study/master/worker_config.jpg "Custom Worker")
