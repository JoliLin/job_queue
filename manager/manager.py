import pathlib
import sys

p = pathlib.Path(__file__).resolve().parent.parent
sys.path.append('{}/'.format(p))
sys.path.append('{}/core'.format(p))

from redis_queue import RedisQueue

#### Redis Cluster
'''
host=
port=

qf = RedisQueue('joli', namespace='hello', version="online", host=host, port=port)
'''

#### Redis
qf = RedisQueue('joli', namespace='hello')

def post_jobs(jobs:list):
    qf.InsertJobs(jobs)

    return 'DONE'

if __name__ == '__main__':
    qf.InsertJobs([1, 2, 3, 4])
