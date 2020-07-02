# xkcd Discord Bot

Sends a daily xkcd comic to a channel of your choice, or you can ask it for a comic.

## Setup

Make sure to set your Google Calendar to the same timezone as the Discord Bot. In this case, it's the timezone of the Compute Engine on Google Cloud.

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