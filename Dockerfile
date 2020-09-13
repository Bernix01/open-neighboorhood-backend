FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv
RUN pipenv sync
COPY . .
