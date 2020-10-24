import { json, Router } from 'express';

import { postAuthenticatedUser } from './routeHandlers';

const routes = Router();

routes.use(json());

routes.post('/', postAuthenticatedUser);

export default routes;
