# Test python task

## before you launch the application, you should fill in the .env file.
## For example:

    DB_USERNAME=ilya
    DB_PASSWORD=12345
    DB_HOST=task_python_db_1 (docker container name)
    DB_PORT=5432
    DB_NAME=test_db
    SECRETE_KEY=my_secrete
    ACCESS_TOKEN_EXPIRE_MINUTES=30

## Runing with docker

    docker-compose build
    docker-compose  up

## Initial migrations

    alembic revision -m "initial migration"
    
### Developed by [Mirolyubov Ilya](https://github.com/M-ILIA-I)