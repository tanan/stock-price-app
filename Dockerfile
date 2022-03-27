FROM python:latest

WORKDIR /app

COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY yahoo_finance_api.py /app/yahoo_finance_api.py

CMD ["python", "main.py"]