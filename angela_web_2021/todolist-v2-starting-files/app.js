//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const date = require(__dirname + "/date.js");

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static("public"));

mongoose.connect("mongodb://localhost:27017/todolistDB", {
  useNewUrlParser: true
});

const itemSchema = {
  name: String
};

const Item = mongoose.model("Item", itemSchema);
const item1 = new Item({
  name: "Welcome to your todolist!"
});

const item2 = new Item({
  name: "Hit the button to add a new item."
});

const item3 = new Item({
  name: "<-- Hit this to delete an item."
});

const defaultItems = [item1, item2, item3];
// const items = ["Buy Food", "Cook Food", "Eat Food"];
// const workItems = [];
const listSchema = {
  name: String,
  items: [itemSchema]
};
const List = mongoose.model("List", listSchema);


app.get("/", function(req, res) {
  Item.find({}, function(err, foundItems) {
    if (foundItems.length === 0) {
      Item.insertMany(defaultItems, function(err) {
        if (err) {
          console.log("err: ", err);
        } else {
          console.log("Successfully saved default items to DB.");
        }
      });
      res.redirect("/");
    } else {
      console.log("Found: ", foundItems);
    }
    res.render("list", {
      cateId: " ",
      listTitle: "Today",
      newListItems: foundItems
    });
  })

});

app.post("/", function(req, res) {
  const itemName = req.body.newItem;
  const listName = req.body.listTitle;
  console.log("body: ", req.body);
  const item = new Item({
    name: itemName
  });
  console.log("listName: ", listName);

  if ("Today" === listName) {
    item.save();
    res.redirect("/");
  } else {
    List.findOne({name: listName}, function(err, foundList) {
      if (!err) {
        console.log("foundList: ", foundList);
        foundList.items.push(item);
        foundList.save();
        res.redirect("/" + listName);
      } else {
        console.log("err: ", err);
      }
    })
  }

});


app.get("/:cateId", function(req, res) {
  let cateId = req.params.cateId;
  console.log("cateId: ", cateId)
  List.findOne({
    name: cateId
  }, function(err, foundItems) {
    if (!err) {
      if (!foundItems) {
        const list = new List({
          name: cateId,
          items: defaultItems
        });
        list.save();
        res.redirect("/" + cateId);
      } else {
        console.log("Exist!")
        res.render("list", {
          cateId: cateId,
          listTitle: foundItems.name,
          newListItems: foundItems.items
        });
      }
    }
  });
})


app.get("/about", function(req, res) {
  res.render("about");
});


app.post("/delete", function(req, res) {
  const checkedID = req.body.checkbox;
  Item.findByIdAndRemove(checkedID, function(err) {
    if (!err) {
      console.log("Successfully deleted checked item.")
      res.redirect("/")
    }
  });
});

app.listen(3000, function() {
  console.log("Server started on port 3000");
});
