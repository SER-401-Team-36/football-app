import { RequestHandler } from 'express';

import Token from '../../utilities/Token';

import authenticateUser from '../../db/users/authenticateUser';

const postAuthenticatedUser: RequestHandler = async (req, res) => {
  const { email, password } = req.body;

  const userAuth = await authenticateUser(email, password);

  if (userAuth) {
    const token = Token.generate(userAuth);

    return res.json({ token });
  } else {
    return res.sendStatus(401);
  }
};
