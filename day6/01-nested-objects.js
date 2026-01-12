//bydefault - undefine value (we can take)
//const[t1, t2 , t3=80] = [100, 200 , undefine]
//value Scape ,, (2 )
//typeof null - Object (bug)
//'3'/2 - 1.5 ('3 is string it convert into Number');
//'a'/2 -NaN('a')- number (only in java )
//NaN*2 - NaN
//NaN/2 - NaN
//NaN HAPPEND FAIL CONVERT INTO Number
//typeof NaN - Number
//var y = 5- y==y (true)
//var t = NaN-t==t(false) OLY VALUE IN JAVA SCRIPT NOT EQUAL TO IT SELF
//how to check NaN A VALUE IF IT IS

//numeric seprator 
//var sallary 12_00_00 //improve radiability
//object destructuring base on key
//ARRAY destructuring 
//how did you check quality- dont repeat your self(dry)
//const {'name, networth, power'}
// task 1.1 destructuring

//crtl+click- take to declaration
//ctrl+~ -open &close terminal
// for color- color


// Case 1: City is Trichy
console.log(city);

// Case 2: City is not present
console.log(city); 

const student1 = {
  name: "Abishek",
  age: 20,
  address: {
    city: "Trichy",
    state: "TN",
  },
  hobbies: ["cricket", "football", "carrom"],
  skills: ["Dance", "Violin"],
};

const student2 = {
  name: "Abishek",
  age: 20,
  address: {
    state: "TN",
  },
  hobbies: ["cricket", "football", "carrom"],
  skills: ["Dance", "Violin"],
};

// Default value taken when the value is undefined
// Task - provide default value for city as 'N/A'
const { name = "Surya", skills = ["HTML", "CSS", "Singer"] } = student;

console.log(name, skills);
console.log(city); 






