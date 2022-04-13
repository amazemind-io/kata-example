FROM python:3.9-alpine

WORKDIR /kata

COPY tests /kata/tests

COPY requirements.txt /kata

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "unittest"]