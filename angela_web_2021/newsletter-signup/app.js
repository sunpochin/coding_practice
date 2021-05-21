const bodyParser = require("body-parser")
const express = require("express")
const request = require("request")
const https = require("https")

app = express()
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}))

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/signup.html")
})

app.post("/subscribe_another", function(req, res) {
  res.redirect("/");
})

app.post("/", function(req, res) {
  console.log("req.body: ", req.body.toString() )
  const firstname = req.body.fName;
  const lastname = req.body.lName;
  const email = req.body.email;
  console.log("first: ", req.body.fName, req.body.lName, req.body.email)

  var data = {
    members: [
      {
        email_address: email,
        status: "subscribed",
        merge_fields: {
          FNAME: firstname,
          LNAME: lastname
        }
      }
    ]
  }

  var jsonData = JSON.stringify(data);

  const url = "https://us6.api.mailchimp.com/3.0/lists/61e70f2a45"
  const options = {
    method: "POST",
    auth: "pachinko:4f205585564097b36b114b4e37ef52dd-us6"
  }

  var responseCode;
  const request = https.request(url, options, function(response) {
    console.log("response: ", response.statusCode);
    if (200 === response.statusCode) {
      // res.send("Success!")
      res.sendFile(__dirname + "/success.html");
    } else {
      res.sendFile(__dirname + "/failure.html");
    }
    response.on("data", function(data) {
      // console.log(JSON.parse(data));
    })
  })
  request.write(jsonData);
  request.end();
  // console.log("response 2: ", response.statusCode);
  // console.log("response 3: ", response.statusCode);
})

// for heroku
app.listen(process.env.PORT || 3000, function() {
  console.log("listening on: ", process.env.PORT)
})


//
// 4f205585564097b36b114b4e37ef52dd-us6

// 61e70f2a45
