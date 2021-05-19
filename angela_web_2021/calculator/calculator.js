const express = require('express');
const bodyParser = require('body-parser');


const app = express();
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', function(req, res) {
  // res.send('hello calculator');
  res.sendFile(__dirname + '/index.html');
});

app.post('/', function(req, res) {
  // console.log(req.body);
  var num1 = Number(req.body.num1);
  var num2 = Number(req.body.num2);
  var result = num1 + num2;
  console.log(req.body, ' result: ', result);

  res.send('Result of calculation is: ' + result);
});


app.get('/bmi', function(req, res) {
  // res.send('hello calculator');
  res.sendFile(__dirname + '/bmi.html');
});


app.post('/bmi', function(req, res) {
  var weight = Number(req.body.weight);
  var height = Number(req.body.height);
  var bmi = weight / Math.pow(height, 2);
  res.send('Result of BMI is: ' + bmi);
});



app.listen(3000, function(req, res) {
  console.log('listening on 3000....');
});
