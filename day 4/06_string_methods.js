// var fullName = "hari ram"
// console.log(fullName.toLowerCase());
// console.log(fullName.toLocaleUpperCase());
// strin are immutable (cannot be change)
// var quote = "  DO GOOD,BE GOOD  ";
// console.log(quote.trim()); // trim remove spaces at the end 
// console.log(quote);
// console.log(quote.trimEnd());
// console.log(quote.trimStart());

// task 1.1
// remove the extra space & convert the to lower case
// 'do good, be good'
var quote = "  DO GOOD,BE GOOD  ";
console.log(quote.trim());
console.log(quote.toLowerCase());

//Dot Chaining - continues until same data type 
var loweredAndTrimed = quote
 .trim() // string
  .toLowerCase();

  console.log(lowercase)






  //Task 3.1 - Testcase - dont consider
  //output
  // case 1
  //please enter your fav🍦?: vanilla
  //Yes, we have vanilla in stock

//case 2
//please enter your fav🍦?: stawberry
//we ran out strawbery
var stock1 = "vanilla";
var stock2 = "chocolate";
var stock3 = "butterscotch";
var stock4 = "cotton candy";
var icecreem = prompt(`please enter your fav icecreem`)
 if (icecreem==stock1 || icecreem==stock2 || icecreem==stock3 || icecreem==stock4){
    console.log(`Yes we have  ${icecreem} in stock`);
 } else if (icecreem== stock2){
    console.log(`yes we have ${icecreem} in stock`)
 } else if(icecreem==stock3){
    console.log(`yes we have ${icecreem} in stock`)
 } else if(icecreem==stock4){
    console.log(`yes we have ${icecreem} in stock`)
 } else {
    console.log(`we ran out of ${icecreem}`);
 }


//Task 3.2 - testcase - consider it 
//output
//case 1
//please enter your fav🍦?:vanilla
//Yes, we have vanilla in stock
//  







