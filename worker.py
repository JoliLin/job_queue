import json

from redis_queue import RedisQueue
from queue_function import ExecuteJobs


def process(data):
    ### main process here
    print('# ', json.loads(data) )

if __name__ == '__main__':
    ExecuteJobs(process)
