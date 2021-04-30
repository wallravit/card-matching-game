# CARD MATCHING GAME API


### Route architecture

`GET /:resource/:id`: to get detail of the `resource` by `id`

`POST /:resource/:action`: to do an `action` with the `resource`

`POST /:resource/:id/:action`: to do an `action` with the `resource` by `id`

## Prerequisite

- python 3.8

## Develop

1. git clone

   ```
   # git clone git@github.com:wallravit/card-matching-game.git
   ```

2. install depedencies

   ```
   # pip install -r dependencies/requirements-dev.txt
   ```

3. set PYTHONPATH

   ```
   # export PYTHONPATH=.
   ```

4. start service

   ```
   # ./scripts/start_api.sh
   ```

## Start Database

```
docker compose up db
```

in case of empty database or first run please run script

```
# ./scripts/init_database.sh
```
## API Document

[Postman API Document](https://documenter.getpostman.com/view/2031982/TzK2auF1)
