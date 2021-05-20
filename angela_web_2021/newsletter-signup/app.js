const bodyParser = require("body-parser")
const express = require("express")
const request = require("request")

app = express()
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}))

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/signup.html")
})

app.post("/", function(req, res) {
  console.log("req.body: ", req.body.toString() )
  var first = req.body.fName;
  var last = req.body.lName;
  var email = req.body.email;
  console.log("first: ", req.body.fName, req.body.lName, req.body.email)
})

app.listen(3000, function() {
  console.log("listening on 3000...")
})
