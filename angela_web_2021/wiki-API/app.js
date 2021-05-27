// jshint esversion:6
const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require("mongoose");

const app = express();

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static("public"));

mongoose.connect("mongodb://127.0.0.1:27017/wikiDB", {
  useNewUrlParser: true
});
const wikiSchema = {
  title: String,
  content: String
};
const Article = mongoose.model("articles", wikiSchema);


app.route("/articles/:articleTitle")
  .get(function(req, res) {
    const articleTitle = req.params.articleTitle;
    console.log("articleTitle: ", articleTitle);
    Article.findOne({
      title: articleTitle
    }, function(err, foundArticle) {
      if (foundArticle) {
        res.send("foundArticle: " + foundArticle);
      } else {
        res.send("No article found.");
      }
    });
  })
  .put(function(req, res) {
    Article.update(
      {title: req.params.articleTitle},
      {title: req.body.title, content: req.body.content},
      {overwrite: true},
      function(err) {
        if(!err) {
          res.send("Successfully PUT updated article");
        }
      }
    );
  })
  .patch(function(req, res) {
    console.log("req.body: ", req.body);
    Article.update(
      {title: req.params.articleTitle},
      {$set: req.body},
      function(err) {
        if(!err) {
          res.send("Successfully PATCH updated article to " + req.body);
        } else {
          res.send("err: " + err);
        }
      }
    );
  })
  .delete(function(req, res) {
    Article.deleteOne(
      {title: req.params.articleTitle},
      function(err) {
        if(!err) {
          res.send("Successfully deleted article: " + req.params.articleTitle);
        }
      }
    );
  });

app.route("/articles")
  .get(function(req, res) {
    Article.find({}, function(err, foundItems) {
      if (err) {
        // console.log("err: ", err);
        res.send("err:", err);
      } else {
        // console.log("foundItems: ", foundItems);
        res.send("Successfully added a new article.", foundItems);

      }
    });
    res.send("hello");
  })
  .post(function(req, res) {
    console.log(req.body.title);
    console.log(req.body.content);
    const newArticle = new Article({
      title: req.body.title,
      content: req.body.content
    });
    newArticle.save(function(err) {
      if (!err) {
        res.send("Successfully added a new article.");
      } else {
        res.send("Err: ", err);
      }
    });
  })
  .delete(function(req, res) {
    Article.deleteMany(function(err) {
      if (!err) {
        res.send("Successfully deleted all articles.");
      } else {
        res.send(err);
      }
    });
  });


// app.get("/articles", function(req, res) {
//   Article.find({}, function(err, foundItems) {
//     if (err) {
//       console.log("err: ", err);
//     } else {
//       console.log("foundItems: ", foundItems);
//     }
//   });
//   res.send("hello");
// });
//
//
// app.post("/articles", function(req, res) {
//   console.log(req.body.title);
//   console.log(req.body.content);
//   const newArticle = new Article({
//     title: req.body.title,
//     content: req.body.content
//   });
//   newArticle.save(function(err) {
//     if (!err) {
//       res.send("Successfully added a new article.");
//     } else {
//       res.send("Err: ", err);
//     }
//   });
// });
//
//
// app.delete("/articles", function(req, res) {
//   Article.deleteMany(function(err) {
//     if (!err) {
//       res.send("Successfully deleted all articles.");
//     } else {
//       res.send(err);
//     }
//   });
// });
//

app.listen(3000, function() {

});
