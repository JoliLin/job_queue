FROM python:3.8

WORKDIR /manager
COPY manager .
COPY core /core

CMD python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5566

CMD python /manager/app.py
