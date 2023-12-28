from redis_queue import RedisQueue

q = RedisQueue('rq')

def InsertJobs(jobs:list):
    for i in jobs:
        q.put(i)
        print(i)

def ExecuteJobs(process):
    while 1:
        result = q.get()
        if result:
            process(result)

if __name__ == '__main__':
    InsertJobs([1, 2, 3, 4])
