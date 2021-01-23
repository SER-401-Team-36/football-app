FROM python:3.8-alpine

WORKDIR /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY espn_Players.csv fantasydata_Players.csv ./
COPY scripts ./scripts
COPY migrations ./migrations
COPY app ./app

CMD ["flask", "run", "-h", "0.0.0.0"]
