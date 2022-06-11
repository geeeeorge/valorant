FROM python:3.9-alpine

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /api/requirements.txt

ENV PYTHONPATH .

# Alpineで、Postgresqlと接続するためのCパッケージを追加。
RUN apk add --no-cache --virtual .build-deps postgresql-dev gcc python3-dev musl-dev \
    && python3 -m pip install --upgrade pip setuptools \
    && python3 -m pip install -r /api/requirements.txt --no-cache-dir \
    && apk --purge del .build-deps


EXPOSE 8943

COPY . /api

# ローカルのときはこのCMDは実行されない
CMD [ "./bin_entrypoints/run_prod.sh" ]
