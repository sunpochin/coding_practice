var numberOfDrums = document.querySelectorAll(".drum").length;

for (var i = 0; i < numberOfDrums; i++) {
  document.querySelectorAll(".drum")[i].addEventListener("click", function() {
    var buttonInnerHTML = this.innerHTML;
    makeSound(buttonInnerHTML);
    // console.log(this.innerHTML);
    // this.style.color = "white";
    // this.inner styles.color = "white";
    // var audio = new Audio("sounds/tom-1.mp3");
    // audio.play();
  });
}

document.addEventListener("keydown", function(event) {
    console.log("event: ", event);
    makeSound(event.key);
});

function makeSound(key) {
  console.log("key: ", key);
  switch (key) {
    case "w":
      var audio = new Audio("sounds/tom-1.mp3");
      audio.play();
    break;
    case "a":
      var audio = new Audio("sounds/tom-2.mp3");
      audio.play();
    break;
    case "s":
      var audio = new Audio("sounds/tom-3.mp3");
      audio.play();
    break;
    case "d":
      var audio = new Audio("sounds/tom-4.mp3");
      audio.play();
    break;
    case "j":
      var audio = new Audio("sounds/crash.mp3");
      audio.play();
    break;
    case "k":
      var audio = new Audio("sounds/kick-bass.mp3");
      audio.play();
    break;
    case "l":
      var audio = new Audio("sounds/snare.mp3");
      audio.play();
    break;
    default:
      console.log("button:", buttonInnerHTML);
  }

};
