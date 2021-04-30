# CARD MATCHING GAME API


### Game Instructions
1. create user
2. generate token key
3. let play


### Board Payload
- Example 3 x 4
```
🃏 🃏 🃏 🃏
🃏 🃏 🃏 🃏
🃏 🃏 🃏 🃏
```

- Board game payload
```
# (row, col)
[
   (1,1), (2,1), (3,1), (4,1), 
   (1,2), (2,2), (3,2), (4,2), 
   (1,3), (2,3), (3,3), (4,3)
]

# example new game board
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

***
```
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
