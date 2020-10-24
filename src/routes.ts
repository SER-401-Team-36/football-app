import { Router } from 'express';

import verifyAuthentication from './authentication/middleware/verifyAuthentication';
import authenticateRoutes from './authentication/routes';
import loanRequestRoutes from './loanRequests/routes';

const authenticatedRoutes = Router();
const routes = Router();

routes.use('/authenticate', authenticateRoutes);

authenticatedRoutes.use(verifyAuthentication);
authenticatedRoutes.use('/loan_requests', loanRequestRoutes);

routes.use(authenticatedRoutes);

export default routes;
