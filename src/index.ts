import express from 'express';

import routes from './routes';

const port = process.env.PORT || '';

const app = express();

app.use(routes);

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
