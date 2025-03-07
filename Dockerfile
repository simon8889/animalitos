FROM python:3.12.9-alpine

WORKDIR /APP

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

COPY . .

RUN pip install poetry
RUN poetry install --no-root

EXPOSE 8000
CMD ["poetry", "run", "fastapi", "run"]

