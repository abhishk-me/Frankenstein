FROM python:3.9-slim

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY . /app
COPY . /pyproject.toml ./

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]