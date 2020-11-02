# football-app
A flask based web app used to run data analysis on football players to determine best fantasy football draft order.

## Database stuff
This app uses flask-sqlalchemy and flask-migrate to handle the connection to PostgreSQL. It relies on the following env variables to be set:
- DB_USERNAME
- DB_PASSWORD
- DB_HOST
- DB_PORT
- DB_DATABASE


## Running the app locally
1. Follow the basic (Flask Installation Guide)[https://flask.palletsprojects.com/en/1.1.x/installation/] to setup flask and python.
2. Set the necessary ENV variables in a local `.env` file at the root of the project. (flask requires some basice ENV variables set to run)
3. Run `flask run`
