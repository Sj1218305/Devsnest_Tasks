let list = document.getElementById("todo-container");

function getTodos(){
  let todos = localStorage.getItem("todos");
  console.log(todos);
  list.innerHTML = todos;
}

function addTodo(e) {
  if(e.code === "Enter"){
    todoInput = document.getElementById('todo-input');
    let todo = todoInput.value;
    if(todo){
      let li= document.createElement("li");
      let span = document.createElement("span");
      let icon = document.createElement("i");
      icon.classList.add("fa");
      icon.classList.add("fa-trash");
      span.appendChild(icon);
      let todoNode = document.createTextNode(todo)
      li.appendChild(todoNode);
      li.insertBefore(span,todoNode);
      document.getElementById("todo-container").appendChild(li);
      localStorage.setItem("todos", list.innerHTML);
      todoInput.value = "";
    }
    else{
      alert("Please add a to-do");
    }
  }
}

document.getElementById("add-new").addEventListener('click', function(){
  document.getElementById("todo-input").classList.toggle("add");
})

document.querySelector("ul").addEventListener("click", function(e){
  if(event.target.tagName === "LI"){
    e.target.classList.toggle("completed");
  }
  localStorage.setItem("todos", list.innerHTML);
});

document.querySelector("ul").addEventListener("click", function(e){
  if(event.target.tagName === "I"){ 
    event.target.parentElement.parentElement.remove();
  }
  if(event.target.tagName === "SPAN"){
    event.target.parentElement.remove();
  }
  localStorage.setItem("todos", list.innerHTML);
});