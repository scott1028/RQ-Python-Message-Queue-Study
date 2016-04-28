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
# 你可以啟動很多个 Worker 他們會分擔 Queue 內的工作！甚至你可以把 Job Producer 跟 Job Cumsumer 放在不同台機器！
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
# timeout: job 應該在 20 秒內被執行否則就 Timeout 被列為失敗佇列
# timeout: job 應該在 20 秒內被執行否則就 Timeout 被列為失敗佇列, Timeout 會被中斷 Job 執行，也就是強制 kill，但是先前已經執行過得部份仍然有效。
# By default, jobs should execute within 180 seconds.
result_fd = q.enqueue(count_words_at_url, 'http://nvie.com')
result_fd = q.enqueue_call(count_words_at_url, 'http://nvie.com', result_ttl=20)
# result_fd = q.enqueue_call(func=count_words_at_url, args=('http://nvie.com',), result_ttl=20, timeout=20)

# 當下不會有結果因為是 Async 的
print result_fd.result

import time
time.sleep(1)

# 等個幾秒可以得到正確結果
# Executing Result Message 保存預設是 500 秒。
print result_fd.result
```

#### Others

- ref: https://pypi.python.org/pypi/redis
- ref: http://python-rq.org/docs/results/
- ref: http://python-rq.org/docs/exceptions/  (Job Fail 的處理機制)

![Alt text](https://raw.githubusercontent.com/scott1028/RQ-Python-Message-Queue-Study/master/worker_config.jpg "Custom Worker")

- Client Result Message 控管(由 Producer 控制)
```
q.enqueue_call(func=foo)  # result expires after 500 secs (the default)
q.enqueue_call(func=foo, result_ttl=86400)  # result expires after 1 day
q.enqueue_call(func=foo, result_ttl=0)  # result gets deleted immediately
q.enqueue_call(func=foo, result_ttl=-1)  # result never expires--you should delete jobs manually
```

#### Monitor Dashboard
```
$ pip install rq-dashboard
$ rq-dashboard
```
