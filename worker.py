from main import process
from redis_queue import RedisQueue

q = RedisQueue('rq')
while 1:
    result = q.get()
    if result:
        process(result)
