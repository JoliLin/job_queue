import pathlib
import sys

p = pathlib.Path(__file__).resolve().parent.parent
sys.path.append('{}/'.format(p))
sys.path.append('{}/core'.format(p))

import json
from loguru import logger
from redis_queue import RedisQueue

def process(data):
    ### main process here
    data = json.loads(data)
    logger.info('# {}'.format(data))

    return 'DONE'

if __name__ == '__main__':
    #### Redis Cluster
    '''
    host="cache-data-tokyo.1itfvt.clustercfg.apne1.cache.amazonaws.com"
    port=6379 
    qf = RedisQueue('joli', namespace='hello', version="online", host=host, port=port)
    '''
    ### Redis
    qf = RedisQueue('joli', namespace='hello')
    qf.ExecuteJobs(process)
