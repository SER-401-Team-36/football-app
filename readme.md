# football-app
A flask based web app used to run data analysis on football players to determine best fantasy football draft order.

## Database stuff
This app uses flask-sqlalchemy and flask-migrate to handle the connection to PostgreSQL. It relies on the `DATABASE_URI` env variable to be set.


## Running the app locally
1. Follow the basic [Flask Installation Guide](https://flask.palletsprojects.com/en/1.1.x/installation/) to setup flask and python.
2. Install all the basic dependancies with `pip install -r requirements.txt`
2. Set the necessary ENV variables in a local `.env` file at the root of the project. (flask requires some basice ENV variables set to run)
  - This includes the `DATABASE_URI`, which should point to your local postgres instance (this should typically look like: `postgres://username:password@localhost:5432/db_name`)
3. Run `flask run`


## Linting
This repo uses [flake8](https://pypi.org/project/flake8/2.2.4/) as a code formater. Please be sure to run `flake8 app` and fix any issues before committing any code, otherwise it will nott pass ci