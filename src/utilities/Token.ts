import { sign, verify } from 'jsonwebtoken';

import User from '../types/User';

const Token = {
  generate: (userId: User['id']): string => {
    return sign({ id: userId }, process.env.TOKEN_SECRET || 'secretTime');
  },

  validate: (token: string): User['id'] | null => {
    try {
      const payload = verify(token, process.env.TOKEN_SECRET || 'secretTime');

      if (typeof payload === 'string') {
        return null;
      }

      return (payload as { id: User['id'] }).id;
    } catch {
      return null;
    }
  },
};

export default Token;
