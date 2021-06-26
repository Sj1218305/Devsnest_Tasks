let bookedSeats = 0;
let RemainingSeats = 400;
let remainingCount = document.getElementById('remaining-count')
let bookedCount = document.getElementById('booked-count')

for(var i =0;i<400;i++){
document.getElementById("container").innerHTML += `<div class="box"></div>`
}

document.getElementById("container").addEventListener('click', function(e){
if(e.target.classList.contains("switch")){
  RemainingSeats++;
  bookedSeats--;
  remainingCount.innerHTML = RemainingSeats;
  bookedCount.innerHTML = bookedSeats;
  e.target.classList.remove("switch");
}else{
  RemainingSeats--;
  bookedSeats++;
  remainingCount.innerHTML = RemainingSeats;
  bookedCount.innerHTML = bookedSeats;
  e.target.classList.add("switch");
}
  
})