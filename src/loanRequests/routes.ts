import { Router } from 'express';

import { getLoanRequests } from './routeHandlers';

const routes = Router();

routes.get('/', getLoanRequests);

export default routes;
