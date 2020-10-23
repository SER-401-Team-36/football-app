# lending-app

# Local Development
This application uses dotenv for local development. To set local environment variables, make a copy of the `.env.example` file and remove the `.example` from the file name. You can then set any local environment variables you need by creating a new line in the file in the form `KEY=value`
Using the `start:dev` command runs the app in watch mode. If any changes are made to a typescript file, the processs will restart automatically.

## Database
This application relies on a local running version of postgres and local env variables set for the `DB_USER` and `DB_PASSWORD` (which can be added to a local `.env` file)
To create your initial database, run the `yarn db:create` command. Then, to run all migrations, use the command `yarn db:up`. To reverse the migrations you can run the `yarn db:down` command. Both of these commands take any arguments that could normally be passed to the [db-migrate](https://db-migrate.readthedocs.io/en/latest/Getting%20Started/commands/) commands
To create a new migration, use the `yarn db:generate` command, followed by the name of the migration.