//Creates light box behavior for an image gallery

var $overlay = $('<div id="overlay"></div>');
var $image = $("<img>");
var $caption = $("<p></p>");

$overlay.append($image);
$overlay.append($caption);
$("body").append($overlay);


$("#imageGallery a").click(function(event){
  //prevent browswer from following link
  event.preventDefault();
  //store image's location in variable
  var imageLocation = $(this).attr("href");
  //set the image file name to a variable
  $image.attr("src", imageLocation);
  //reveal overlay
  $overlay.show();
  //store the image's alt text in a variable
  var captionText = $(this).children("img").attr("alt")
  //fill the image caption with the alt text
  $caption.text(captionText);
});

$overlay.click(function(){
  //hide overlay after the user is finished looking at the photo.
  $overlay.hide();
})
