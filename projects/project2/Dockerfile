FROM python:3-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY features/ ./features/
COPY utils.py .
COPY app.py .

CMD flask run -h 0.0.0.0