import { createPool } from 'slonik';

const connectionString = `postgres://${process.env.DB_USER}:${process.env.DB_PASSWORD}@${process.env.DB_HOST}/lending-app-db`;
const connection = createPool(connectionString);

export default connection;
