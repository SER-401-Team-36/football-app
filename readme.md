# football-app
A flask based web app used to run data analysis on football players to determine best fantasy football draft order.

## Database stuff
This app uses flask-sqlalchemy and flask-migrate to handle the connection to PostgreSQL. It relies on the `DATABASE_URI` env variable to be set (which is set automatically if using docker).

## Docker
This app is now setup with docker. Follow the steps in [Running the app in docker](#Running-the-app-in-docker) to get it set up. If you need to run commands in a container, you can use the command `docker exec [db|web] sh` to get shell access.


## Running the app locally
1. Follow the basic [Flask Installation Guide](https://flask.palletsprojects.com/en/1.1.x/installation/) to setup flask and python.
2. Install all the basic dependancies with `pip install -r requirements.txt`
2. Set the necessary ENV variables in a local `.env` file at the root of the project. (flask requires some basice ENV variables set to run)
    - This includes the `DATABASE_URI`, which should point to your local postgres instance (this should typically look like: `postgres://username:password@localhost:5432/db_name`)
3. If it's the first time running the application, run all the db migrations first with `flask db upgrade`
4. Once you have the db created, run `flask import-players` to seed the db from the provided csv
5. Run `flask run`

## Running the app in docker
(Note that any changes to code will require a restart of the containers to pick up)
1. Install [docker](https://www.docker.com/products/docker-desktop) locally
2. Run `docker-compose up` to start up the containers
3. Open new terminal window, then continue to step 4.
4. Run `docker-compose exec web flask db upgrade` to run all pending migrations
5. Run `docker-compose exec web flask import-players` to run the import script 
6. Switch to Front-End folder (football-app-ui)
7. sudo apt install npm
8. sudo apt-get update
9. npm config set strict-ssl false
10. npm install
11. npm start
12. The default login information is
    - username: user
    - password: password


## Linting
This repo uses [flake8](https://pypi.org/project/flake8/2.2.4/) as a code formater. Please be sure to run `flake8 app` and fix any issues before committing any code, otherwise it will nott pass ci
