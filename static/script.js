function zoomImage(image){


let modal =
document.getElementById(
"imageModal"
);


let popup =
document.getElementById(
"popupImage"
);


popup.src=image.src;


modal.style.display="flex";


}



document
.getElementById("imageModal")
.onclick=function(){


this.style.display="none";


}