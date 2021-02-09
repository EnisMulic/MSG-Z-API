FROM python:3.8

RUN pip3 install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000"]