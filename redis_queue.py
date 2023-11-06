import redis

class RedisQueue():
    def __init__(self, name, namespace='test', **redis_kwargs):
        self.db = redis.Redis(**redis_kwargs)
        self.key = '{}:{}'.format(namespace, name)

    def qsize(self):
        return self.db.llen(self.key)

    def put(self, item):
        return self.db.rpush(self.key, item)

    def get(self):
        return self.db.lpop(self.key)
