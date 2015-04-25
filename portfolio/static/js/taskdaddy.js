//Problem: User interation doesn't provide desired results.
//Solution: Add interactivity to the user can manage daily tasks.

var taskInput = document.getElementById("new-task");
var addButton = document.getElementsByTagName("button")[0];
var incompleteTasksHolder = document.getElementById("incomplete-tasks");
var completedTasksHolder = document.getElementById("completed-tasks");

//New Task List Item
var createNewTaskElement = function(taskString) {
	var listItem = document.createElement("li");
		
	//input(check box)
	var checkBox = document.createElement("input");
	//label
	var label = document.createElement("label");
	//input(text)
	var editInput = document.createElement("input");
	//button.edit
	var editButton = document.createElement("button");
	//button.delete
	var deleteButton = document.createElement("button");
	
	//each element needs to be modified
	checkBox.type = "checkbox";
	editInput.type = "text";

	editButton.innerText = "Edit";
	editButton.className = "edit";

	deleteButton.innerText = "Delete";
	deleteButton.className = "delete";

	label.innerText = taskString;




	//each element needs to be appended
	listItem.appendChild(checkBox);
	listItem.appendChild(label);
	listItem.appendChild(editInput);
	listItem.appendChild(editButton);
	listItem.appendChild(deleteButton);


	return listItem;
}

//Add a new task
var addTask = function() {
	console.log("Add task...");	
//when the button is pressed
	//create a new list item with the text from #new-task:
	var listItem = createNewTaskElement(taskInput.value);
	incompleteTasksHolder.appendChild(listItem);
	bindTaskEvents(listItem, taskCompleted);
	taskInput.value = "";
}


//edit an existing task
var editTask = function(){
	console.log("Edit task...");
	var listItem = this.parentNode;
	var editInput = listItem.querySelector("input[type=text");
	var label = listItem.querySelector("label");

	//if the class of the parent is.editMode
	if(listItem.classList.contains("editMode")) {
		//switch from .editMod
		//label text becomes the input's value
		label.innerText = editInput.value;
	}

	else {
		//switch from .editMode
		//input value becomes the label's text
		editInput.value = label.innerText;
	}

	//toggle .editMode on the parent
	listItem.classList.toggle("editMode");

}


//Delete an existing task
var deleteTask = function() {
	console.log("Delete task...");
	var listItem = this.parentNode;
	var ul = listItem.parentNode;

	//remove the parent list item from the ul
	ul.removeChild(listItem);
}



//mark a task as complete
var taskCompleted = function() {
	console.log("Task Completed...");
	//append the task list item to the #completed-tasks
	var listItem = this.parentNode;
	completedTasksHolder.appendChild(listItem);
	bindTaskEvents(listItem, taskIncomplete);
}


//Mark a task as incomplete
var taskIncomplete = function() {
  console.log("Task incomplete...");
  //When the checkbox is unchecked
    //Append the task list item to the #incomplete-tasks
    var listItem = this.parentNode;
    incompleteTasksHolder.appendChild(listItem);
    bindTaskEvents(listItem, taskCompleted);
}



var bindTaskEvents = function(taskListItem, checkBoxEventHandler) {
	console.log("Bind list item events");
	//select taskListItem's children
	var checkBox = taskListItem.querySelector("input[type=checkbox]");
	var editButton = taskListItem.querySelector("button.edit");
	var deleteButton = taskListItem.querySelector("button.delete");

	//bind editTask to edit button
	editButton.onclick = editTask;

	//bind deleteTask to delete button
	deleteButton.onclick = deleteTask;

	//bind checkBoxEventHandler to checkbox
	checkBox.onchange = checkBoxEventHandler;


}


//set the click handler to the addtask function
addButton.onclick = addTask;


//cycle over incompleteTasksHolder ul list items
for(var i = 0; i < incompleteTasksHolder.children.length; i++) {
	//bind events to list item's children (taskCompleted)
	bindTaskEvents(incompleteTasksHolder.children[i], taskCompleted);
}


//cycle over completedTasksHolder ul list items
for(var i = 0; i < completedTasksHolder.children.length; i++) {
	//bind events to list item's children (taskIncomplete)
	bindTaskEvents(completedTasksHolder.children[i], taskIncomplete);
}