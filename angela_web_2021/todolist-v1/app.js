//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const date = require(__dirname + "/date.js")
console.log('date: ', date)


let items = ["buy food", "cooking", "have lunch!"];
let workitems = [];

const app = express();
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/", function(req, res){
  let day = date();
  res.render("list", {listTitle: day, newItems: items} );
});

app.post("/", function(req, res) {
  console.log("req.body: ", req.body)
  item = req.body.newitem;
  if (item.length === 0) {
    return;
  }
  if (req.body.list === "Work") {
    workitems.push(item)
    res.redirect("/work");
  } else {
    items.push(item);
    res.redirect("/");
  }
})


app.get("/work", function(req, res) {
  res.render("list", {listTitle: "Work List", newItems: workitems})
})


app.post("/work", function(req, res) {
  console.log("req.body: ", req.body)
  item = req.body.newitem;
  if (item.length === 0) {
    return;
  }
  workitems.push(item);
  console.log("item: ", item)
  res.redirect("/work");
})


app.get("/about", function(req, res) {
  res.render("about");
});


app.listen(3000, function(){
  console.log("Server started on port 3000.");
});
