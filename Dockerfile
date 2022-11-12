FROM python:3.9.6

WORKDIR /app

COPY req.txt req.txt

RUN pip3 install -r req.txt

COPY . .
  
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
