from redis_queue import RedisQueue

q = RedisQueue('rq')

for i in range(5):
    q.put(i)

    print(i)
