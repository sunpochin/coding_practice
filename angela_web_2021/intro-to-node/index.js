//var fs = require('fs');
const fs = require("fs");
fs.copyFileSync("file1.txt", "file2.txt")

console.log("hello world");


var superheroes = require("superheroes");

var name = superheroes.random();
console.log("hero: ", name);

var supervillains = require("supervillains");
var villain = supervillains.random();
console.log("villain: ", villain);
