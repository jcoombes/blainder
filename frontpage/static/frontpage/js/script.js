'use strict';

let frame = document.querySelector(".polaroid-frame");
let dislikebutton = document.getElementById("dislike");
let likebutton = document.getElementById("like");

frame.addEventListener("transitionend", frame.remove);
dislikebutton.addEventListener("click", () => {pile('left');});
likebutton.addEventListener("click", () => {pile('right');});


function pile (choice) {
  // leftpile: bool - if True, place card on left pile.
  // else place card on right pile.
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
  imgnode.src = getnextimagesrc();
  imgnode.alt = getnextimagealt();



  newframe.addEventListener("transitionend", frame.remove);
}

function getnextimagesrc () {
  //This will make an ajax call to the server to get the next picture
  //of blaine from the database.
  //
  fetch('https://jsonplaceholder.typicode.com/photos/1')
  .then(response => response.json())
  .then(json => console.log(json))
  return "https://cdn.bulbagarden.net/upload/thumb/c/c8/Lets_Go_Pikachu_Eevee_Blaine.png/216px-Lets_Go_Pikachu_Eevee_Blaine.png";
}

function getnextimagealt () {
  //same as src, but it finds the alt attribute.
  //I think I want to have a function query the server
  //and this function and the function above just parse the result when it returns.
  return "The Hotheaded Quiz Master!"
}