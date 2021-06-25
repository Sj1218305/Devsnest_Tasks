let container = document.getElementById("todo-container");

function getTodos(){
  let todos = localStorage.getItem("todos");
  console.log(todos)
  container.innerHTML = todos;
}
function addTodo(e){
  if(e.code === "Enter"){
      let todo = document.getElementById('todo-input').value;
      if(todo){
        document.getElementById("todo-container").innerHTML += `<li><span><i class="fa fa-trash"></i></span>${todo}</li>`
      document.getElementById('todo-input').value = "";
      }else{
        alert("Please enter some value");
      }
  }
  localStorage.setItem("todos", container.innerHTML);
}

document.getElementById("addNew").addEventListener("click", function(){
  document.getElementById("todo-input").classList.toggle("showInput");
})

document.querySelector("ul").addEventListener("click", function(e){
  e.target.classList.toggle("completed");
  localStorage.setItem("todos", container.innerHTML);
});


document.querySelector("ul").addEventListener("click", function(e){
  if(e.target.tagName === "I")
  e.target.parentElement.parentElement.remove();
  else if(e.target.tagName === "SPAN")
  e.target.parentElement.remove();
  localStorage.setItem("todos", container.innerHTML);
});

  