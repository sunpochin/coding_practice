
const express = require('express');
const https = require('https');



const app = express();

app.get('/', function(req, res) {
  const url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=b6a352bbf52795af4909153e8e98da71';
  https.get(url, function(response) {
    console.log('response: ', response.statusCode);

    response.on('data', function(data){
      console.log('data: ', data);
      const weatherData = JSON.parse(data);
      console.log('weather data: ', weatherData);
      const temp = weatherData.main.temp
      console.log('temp: ', temp);
      
    })
  });

  res.send('server up and running.')

})

app.listen(3000, function() {
  console.log('server running on 3000');
})
