FROM python:3.8

WORKDIR /worker
COPY worker .
COPY core /core

CMD python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD python /worker/worker.py
