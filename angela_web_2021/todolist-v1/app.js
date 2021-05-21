//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");

const app = express();
var items = ["buy food", "cooking", "have lunch!"];
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.get("/", function(req, res){
  var options = { weekday: 'long', year: '2-digit', month: 'long', day: '2-digit' };
  var today  = new Date();

  console.log(today.toLocaleDateString("en-US")); // 9/17/2016
  console.log(today.toLocaleDateString("en-US", options)); // Saturday, September 17, 2016
  console.log(today.toLocaleDateString("hi-IN", options)); // शनिवार, 17 सितंबर 2016
  // day = today.toLocaleDateString("zh-TW", options);
  day = today.toLocaleDateString("ja-JP", options);
  res.render("list", {kindOfDay: day, newItems: items} );
  // res.send("Hello");});
});

app.post("/", function(req, res){
  item = req.body.newitem;
  if (item.length === 0) {
    return;
  }
  items.push(item);
  res.redirect("/");
})

app.listen(3000, function(){
  console.log("Server started on port 3000.");
});
