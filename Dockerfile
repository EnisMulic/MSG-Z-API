# FROM python:3.8

# WORKDIR /app
# COPY . .

# RUN pip install pipenv
# RUN pipenv install --deploy --ignore-pipfile
# RUN pipenv run python migrate.py db upgrade

FROM python:3.8

RUN pip3 install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]

