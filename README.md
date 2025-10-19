# ILIAD ORDER MANAGEMENT




## Project Setup

```sh
docker compose up --build
```

### TO VISUALIZE AND USE FRONTENDAPP OPEN BROWSER ON ADDRESS http://localhost:8080/
### TO VISUALIZE BACKEND SWAGGER open browser on address http://localhost:8080/docs
### TO VISUALIZE  AND USE DJANGO ADMIN open browser on address http://localhost:8080/admin (user: root, pw:root)





## Backend tests

```sh
docker compose up --build
docker compose exec djbackend sh
python manage.py test
```


## DB: if db.sqlite3 should be deleted, to rebuild db and exec migrations

```sh
docker compose up --build
docker compose exec djbackend sh
python manage.py migrate
```

## Frontend APP: to start FE service env and to see realtime changes on pages

```sh
docker compose up --build

```
 ### open a second terminal and exec following commands
 ```sh
CD FE
npm run build
```

### TO VISUALIZE AND USE DEV FRONTENDAPP OPEN BROWSER ON ADDRESS http://localhost:5173/