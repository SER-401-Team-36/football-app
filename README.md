# lending-app

# Local Development
This application uses dotenv for local development. To set local environment variables, make a copy of the `.env.example` file and remove the `.example` from the file name. You can then set any local environment variables you need by creating a new line in the file in the form `KEY=value`
Using the `start:dev` command runs the app in watch mode. If any changes are made to a typescript file, the processs will restart automatically.