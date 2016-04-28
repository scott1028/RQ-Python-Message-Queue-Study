# coding: utf-8

REDIS_URL = 'redis://localhost:6379/1'

# You can also specify the Redis DB to use
# REDIS_HOST = 'redis.example.com'
# REDIS_PORT = 6380
# REDIS_DB = 3
# REDIS_PASSWORD = 'very secret'

# 監聽這幾個 Queue 估計順序就是優先執行權重！
# Queues to listen on
QUEUES = ['high', 'normal', 'low', 'default']

# If you're using Sentry to collect your runtime exceptions, you can use this
# to configure RQ for it in a single step
# SENTRY_DSN = 'http://public:secret@example.com/1'
