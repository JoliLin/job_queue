import redis
from rediscluster import RedisCluster

from loguru import logger

class QueueCore():

    def __init__(self,
                 name,
                 namespace='test',
                 version='redis',
                 **redis_kwargs):
        if version == 'redis':
            self.db = redis.Redis(**redis_kwargs)
        else:
            startup_nodes = [{
                'host': redis_kwargs['host'],
                'port': redis_kwargs['port']
            }]
            self.db = RedisCluster(startup_nodes=startup_nodes,
                                   decode_responses=True,
                                   skip_full_coverage_check=True)
        self.key = '{}:{}'.format(namespace, name)

    def qsize(self):
        return self.db.llen(self.key)

    def put(self, item):
        return self.db.rpush(self.key, item)

    def get(self):
        return self.db.lpop(self.key)


class RedisQueue:

    def __init__(self,
                 name,
                 namespace='test',
                 version='redis',
                 **redis_kwargs):
        self.q = QueueCore(name=name, namespace=namespace, version=version, **redis_kwargs)

    def InsertJobs(self, jobs: list):
        for i in jobs:
            self.q.put(i)
            logger.info('### Insert {} into Queue'.format(i))

    def ExecuteJobs(self, process):
        logger.info('### Start listening')

        while True:
            result = self.q.get()
            if result:
                process(result)
