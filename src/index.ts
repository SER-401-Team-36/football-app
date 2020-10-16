import express from 'express';

const port = process.env.PORT || '';

const app = express();

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
