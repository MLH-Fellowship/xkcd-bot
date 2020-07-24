# xkcd Discord Bot

Sends a daily xkcd comic to a channel of your choice, or you can ask it for a comic.

![Docker Image CI](https://github.com/MLH-Fellowship/xkcd-bot/workflows/Docker%20Image%20CI/badge.svg)

![Deploying to Google Compute Engine](https://github.com/MLH-Fellowship/xkcd-bot/workflows/Deploying%20to%20Google%20Compute%20Engine/badge.svg)

## Setup
```
docker build -t xkcd-bot .
cp example.env .env
```

_Make sure to fill the `.env` file with the required fields_

## Run

```
docker run --name xkcd-bot --env-file .env -d xkcd-bot
```

Alternatively build and run with `docker-compose`:

```bash
docker-compose build
docker-compose up -d
docker-compose logs -f
```
