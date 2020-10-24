import { RequestHandler } from 'express';

import authenticateUser from '../../db/users/authenticateUser';
import Token from '../../utilities/Token';

const postAuthenticatedUser: RequestHandler = async (req, res) => {
  const { email, password } = req.body;

  const userAuth = await authenticateUser(email, password);

  if (userAuth) {
    const token = Token.generate(userAuth);

    res.json({ token });
  } else {
    res.sendStatus(401);
  }
};

export default postAuthenticatedUser;
