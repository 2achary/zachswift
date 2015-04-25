//Prevent spoilerphobes from seeing spoilers
//Solution: Hide spoilers and reveal them through user interaction

//hide all spoiler spans
$(".spoiler span").hide();
//add a button
$(".spoiler").append("<button>Reveal Spoiler!</button>")
//when button is pressed, 
$("button").click(function(){
	$(this).prev().show();
	$(this).remove();
});
	//show the spoiler
	//get rid of button