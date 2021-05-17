var randomNumber1 = Math.floor(Math.random() * 6) + 1;
document.querySelector(".img1").setAttribute("src", "images/dice" + randomNumber1 + ".png");

var randomNumber2 = Math.floor(Math.random() * 6) + 1;
document.querySelector(".img2").setAttribute("src", "images/dice" + randomNumber2 + ".png");

// <img src="images/dice" + randomNumber1 + ".png" alt="flowers">

var newtext = ""
if (randomNumber1 > randomNumber2) {
  newtext = "Player 1 Wins!";
} else if (randomNumber1 < randomNumber2) {
  newtext = "Player 2 Wins!";
} else if (randomNumber1 === randomNumber2) {
  newtext = "Draw!";
}

document.querySelector("h1").innerText = newtext;
