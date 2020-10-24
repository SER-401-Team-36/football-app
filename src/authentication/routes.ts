import { Router, json } from 'express';

const routes = Router();

routes.use(json());

routes.get('/');
