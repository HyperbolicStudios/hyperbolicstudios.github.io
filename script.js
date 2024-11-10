

  window.onscroll = function() {myFunction()};
function myFunction() {

  var element = document.getElementById("mainHeader");
  var class_name = element.className;


  var h = (window.innerHeight)*.4;

console.log(document.body.scrollTop);
  if (((document.body.scrollTop + document.documentElement.scrollTop) > h) && class_name != "slideUp") {

    element.classList.add("slideUp");


    element.style.transform = "translateY(0)";


    console.log("done");

  }

  else if ((document.body.scrollTop + document.documentElement.scrollTop) < h && class_name == "slideUp"){
  document.getElementById("mainHeader").classList.remove("slideUp");
  console.log("remove");
  element.style.transform = "translateY(-15vh)";
}}

function openNav() {
  document.getElementById("menu").style.transform = "translateX(0)";
}

function closeNav() {
  document.getElementById("menu").style.transform = "translateX(100%)";
}


$(document).ready(function(){
  var screenWidth = $(window).width();
  console.log("Mobile evaluation done");
  // if window width is smaller than 800 remove the autoplay attribute
  // from the video
  if (screenWidth > 800){
      document.getElementById("videoContent").src = "static/videos/vid1.webm";
      var video = document.getElementById('video');
video.load();
video.play();
        console.log("Video enabled");
}
  else {
    console.log("Video NOT enabled");
  }
});
