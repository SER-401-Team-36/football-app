import User from '../types/User';

import { sign } from 'jsonwebtoken';

import { validate } from 'jsonwebtoken';

const Token = {
  generate: (userId: User['id']) => {
    return sign({ id: userId }, process.env.TOKEN_SECRET || '');
  },
};

export default Token;
