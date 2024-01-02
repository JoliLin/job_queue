import pathlib
import sys

p = pathlib.Path(__file__).resolve().parent.parent
sys.path.append('{}/'.format(p))
sys.path.append('{}/core'.format(p))

import uvicorn
from fastapi import FastAPI, Depends

from manager import post_jobs

app = FastAPI()

@app.post("/api/post_jobs")
def post_jobs(commons: dict=Depends(post_jobs)):
    return commons

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=5566, reload='debug'=='debug')

