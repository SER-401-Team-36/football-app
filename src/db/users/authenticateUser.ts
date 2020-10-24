import { sql } from 'slonik';

import connection from '../connection';

import User from '../../types/User';

const authenticateUser = async (email: string, password: string): Promise<User['id'] | null> => {
  try {
    const user = await connection.one<{ id: User['id'] }>(sql`
    SELECT id
    FROM Users
    WHERE email = ${email}
      AND password = crypt(${password}, password)
    `);

    return user.id;
  } catch {
    return await null;
  }
};

export default authenticateUser;
