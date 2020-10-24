import { RequestHandler } from 'express';

import Token from '../../utilities/Token';

const verifyAuthentication: RequestHandler = (req, res, next) => {
  const [authType, authCredentials] = req.headers.authorization?.split(' ') || ['', ''];
  const userId = Token.validate(authCredentials);

  if (authType === 'Bearer' && userId) {
    req.userId = userId;
    next();
  } else {
    res.sendStatus(401);
  }
};

export default verifyAuthentication;
