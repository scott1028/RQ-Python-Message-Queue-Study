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
# timeout: job 應該在 20 秒內被執行否則就 Timeout 被列為失敗佇列, Timeout 會被中斷 Job 執行，也就是強制 kill，但是先前已經執行過得部份仍然有效。
# >> 從 Client 推送到後到 Redis 後計算兩秒，如果 Worker 事後才啟動就很容易出現 Job Timeout Fail。
# By default, jobs should execute within 180 seconds.
# return 一個 job fd 可以用來存取該 JOB 的資訊。
# result_fd = q.enqueue(count_words_at_url, 'http://nvie.com')
result_fd = q.enqueue_call(func=count_words_at_url, args=('http://nvie.com',), result_ttl=20)
# result_fd = q.enqueue_call(func=count_words_at_url, args=('http://nvie.com',), result_ttl=20, timeout=20)

# 當下不會有結果因為是 Async 的
print result_fd.result

import time
time.sleep(1)

# 等個幾秒可以得到正確結果
# Executing Result Message 保存預設是 500 秒。
print result_fd.result

# More Information
print result_fd.get_id()
print result_fd.status
print result_fd.to_dict()
import pdb; pdb.set_trace()
