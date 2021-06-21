// Function to check whether an `input` is an array or not

const checkArray = (item) => {
    if(Array.isArray(item))
        return true;
    else
        return false;
}

// Function to clone an array

const shallowCopy = (item) => {
	const duplicate = item;
	return duplicate;
}

const deepCopy = (item) => {
	const duplicate = JSON.parse(JSON.stringify(item));;
	return duplicate;
}

	

const ReturnNElements = (item,n) => {
	if(n < 0 || item == [])
		return [];
	else if(n == undefined){
		return item[0];
	}
	else{
		const ans = [];
		for(int i =0;i<item.length() && i<n;i++){
			ans.push(item[i]);
		}
		return ans;
	}
}

// Function to join all elements of the following array into a string.

const concatenate = (item) => {
	let ans = "";
	item.forEach((x) => {
		ans += x + ',';
	})
	return ans.substr(0, ans.length -1);
}


// Function to find an element with maximum frequency inside an array.

const frequentElement = (item) => {
	let max_freq = 0;
	let max_element;	
	let hashmap = {};
	item.forEach((x) => {
		if(hashmap[x]){
			hashmap[x]++;
		}else{
			hashmap[x] = 1;
		}
	})
	Object.entries(hashmap).forEach(entry => {
		const [key,value]  = entry;
		if(value > max_freq){
			maximum = value;
			max_element = key;
		}
	})
	return max_element;
}


