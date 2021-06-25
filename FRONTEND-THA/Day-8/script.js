for(var i =0;i<400;i++){
document.getElementById("container").innerHTML += `<div class="box"></div>`
}

document.getElementById("container").addEventListener('click', function(e){
	e.target.classList.toggle("switch");
})