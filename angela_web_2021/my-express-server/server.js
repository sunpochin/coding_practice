const express = require('express');
const app = express();

app.get('/', function(request, response) {
  console.log(request);
  response.send('<h1>Hello express! </h1>');
});

app.get('/contact', function(req, res) {
  res.send('contact sunpochin');
});

app.get('/about', function(req, res) {
  res.send('I am sunpochin, a software developer.');
});


// app.get('/', (req, res) => res.send('Hello express!'));

app.listen(3000, () => console.log('Example app on port 3000...'));
