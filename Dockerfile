FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY packages.txt packages.txt

RUN pip install -r requirements.txt

COPY app.py ./app/app.py
EXPOSE 8501

CMD ["streamlit", "run", "./app/app.py"]