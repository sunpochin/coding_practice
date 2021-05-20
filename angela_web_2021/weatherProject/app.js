
const express = require('express');
const https = require('https');
const bodyParser = require("body-parser");


const app = express();
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', function(req, res) {
  res.sendFile(__dirname + "/index.html");
})


app.post('/', function(req, res) {
  console.log(req.body.cityName);
  // console.log("Post request received.")
  const city = req.body.cityName;
  const apikey = "b6a352bbf52795af4909153e8e98da71";
  const unit = "metric";
  const url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apikey + "&units=" + unit;
  https.get(url, function(response) {
    console.log('response: ', response.statusCode);

    response.on('data', function(data){
      // console.log('data: ', data);
      const weatherData = JSON.parse(data);
      // console.log('weather data: ', weatherData);
      const temp = weatherData.main.temp
      console.log('temp: ', temp);
      const weatherDesc = weatherData.weather[0].description
      const icon = weatherData.weather[0].icon
      const imgUrl = "http://openweathermap.org/img/wn/" + icon + "@2x.png";
      res.write('<p>The Weather is currently ' + weatherDesc + '<p>');
      res.write("<h1>The temperature in " + city + " is: " + temp + " degrees Celcius. </h1>");
      res.write("<img src=" + imgUrl + ">");
      res.send();
    })
  });
})



// res.send('server up and running.')
//


app.listen(3000, function() {
  console.log('server running on 3000');
})
