import { RequestHandler } from 'express';

import getAllLoanRequests from '../../db/loanRequests/getAllLoanRequests';

const getLoanRequests: RequestHandler = async (req, res) => {
  const loanRequests = await getAllLoanRequests();

  res.send(loanRequests);
};

export default getLoanRequests;
