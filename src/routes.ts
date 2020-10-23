import { Router } from 'express';

import loanRequestRoutes from './loanRequests/routes';

const routes = Router();

routes.use('/loan_requests', loanRequestRoutes);

export default routes;
