// Program to list the properties of a JavaScript object

const printKeys = (item) =>{
	var ans  []
	Object.keys(item).map(x => {
    ans.push(x);
	})
	return ans;
}

// Program to delete the rollno property from the object

const deleteKey = (item) =>{
    delete item['rollno'];
	console.log(item);
}

// JavaScript program to get the length of a JavaScript object

const calculateLength = (item) =>{
	return Object.keys(item).length;
}

// JavaScript program to display the reading status 

const displayReadingStatus = (item) => {
	item.forEach((x) => {
		console.log(x['readingStatus']);
	})
}

 // Program to get the volume of a Cylinder (upto 4 decimal Places)

 Cylinder = {
 	radius: 0,
 	height: 0,
 	volume: (radius,height)=>{
 		return (2*3.14*radius*height).toFixed(4);
 	}
 }

 

