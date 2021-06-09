let operation;
let firstInputValue;
let secondInputValue;
let output = document.getElementById("output");

document.querySelectorAll('#add, #subtract,#multiply,#divide').forEach(function(button) {
  button.addEventListener('click', function(e) {
    operation = this.id;
    firstInputValue = Number(document.getElementById("first-input").value);
    secondInputValue = Number(document.getElementById("second-input").value);
    if(isNaN(firstInputValue) || isNaN(secondInputValue)){
      output.innerHTML = "Not a valid Input";
    }
    else{
switch(operation) {
   case "add":
output.innerHTML = firstInputValue+secondInputValue; 
    break;
  case "subtract":
output.innerHTML = firstInputValue-secondInputValue;
    break;
  case "multiply":
output.innerHTML = firstInputValue*secondInputValue;
    break;
  case "divide":
output.innerHTML = firstInputValue/secondInputValue;
    break;    
}
    }
  })
});

