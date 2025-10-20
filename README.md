# ILIAD ORDER MANAGEMENT




## Project Setup
To prepare the env from the root folder in the terminal digit th docker compose command

```sh
docker compose up --build
```

FOR FRONTENDAPP Oopen browser on address http://localhost:8080/
FOR BACKEND SWAGGER open browser on address http://localhost:8080/docs
FOR  DJANGO ADMIN open browser on address http://localhost:8080/admin (user: root, pw:root)





## Backend tests
To run backend test once containers are up from a second terminal enter the djbackend container and use django command to execute tests

```sh
docker compose up --build
docker compose exec djbackend sh
python manage.py test
```


## DB: if db.sqlite3 should be deleted, to rebuild db and exec migrations

The project contains a sqlite3 db already populated with samples, if the sqlite3 file is missing or deleted, to rebuild the db once the backend container is up enter via terminal and run the migrate command

```sh
docker compose up --build
docker compose exec djbackend sh
python manage.py migrate
```

## Frontend APP: to start FE service env and to see realtime changes on pages
 To edit vue app and see realtime chages once the backend container is up form the FE directory you can launch development server through the following commands

```sh
docker compose up --build

```
 ### open a second terminal and exec following commands
 ```sh
CD FE
npm install
npm run build
```
OPEN BROWSER ON ADDRESS http://localhost:5173/