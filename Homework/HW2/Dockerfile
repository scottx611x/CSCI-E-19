FROM python:3.7-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./features /features/
COPY main.py .
CMD behave