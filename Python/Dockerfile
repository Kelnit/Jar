FROM python:3.10-slim

WORKDIR /application

COPY . .

RUN pip install -r requirements.txt

COPY . /application

EXPOSE 8080

CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8080"]