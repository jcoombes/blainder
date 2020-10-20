'use strict';

let frame = document.querySelector(".polaroid-frame");
let dislikebutton = document.getElementById("dislike");
let likebutton = document.getElementById("like");
let times_clicked = 0

frame.addEventListener("transitionend", frame.remove);
dislikebutton.addEventListener("click", () => {pile_with_promises('left', times_clicked++);});
likebutton.addEventListener("click", () => {pile_with_promises('right', times_clicked++);});


function pile_with_promises (choice, times_clicked) {
  fetch(`https://jsonplaceholder.typicode.com/photos/${times_clicked + 1}`)
  .then(response => response.json())
  .then(obj => pile(choice, obj))
}


function pile (choice, obj) {
  // choice - string 'left' or 'right'
  // obj - a fetch object after running response.json()
  let frame = document.querySelector(".polaroid-frame:not(.rotate-left):not(.rotate-right)");
  let newframe = document.createElement("div");
  frame.after(newframe);

  if (choice === 'left') {
    frame.classList.add("rotate-left");
  }
  else {
    frame.classList.add("rotate-right");
  }

  newframe.classList.add("fade-in");
  newframe.classList.add("polaroid-frame");

  let imgnode = document.createElement("img");
  newframe.appendChild(imgnode);
  imgnode.src = obj.url
  imgnode.alt = obj.title

  newframe.addEventListener("transitionend", frame.remove);
  };
