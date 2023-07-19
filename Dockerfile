FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /src

ENV POETRY_HOME=/opt/poetry

RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml* poetry.lock* ./

RUN if [ -f pyproject.toml ]; then poetry install; fi

ENTRYPOINT ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]