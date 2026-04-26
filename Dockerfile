FROM python:3.11.15-slim-trixie

WORKDIR /app

RUN pip install "fastapi[standard]"

COPY . /app/

EXPOSE 8000

CMD ["fastapi", "dev"]