 //Task 1.1
// Output
// Hulk contains 4 letters
// Iron man contains 8 letters
// ...
// Thor contains 4 letters

// const avengers = [
//   "Hulk",
//   "Iron man",
//   "Black widow",
//   "Captain america",
//   "Spider man",
//   "Thor",
// ];
// for(let index =0;index < avengers.length;index++){
//  console.log(`${avengers[index]} contains ${avengers[index].length} letters`);

// };

// const avengers = [
//   "Hulk",
//   "Iron man",
//   "Black widow",
//   "Captain america",
//   "Spider man",
//   "Thor",
// ];

// for (let avenger of avengers) {
//   console.log(avenger);
// }

// const books = [
//          {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
//     {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
//     {"title": "Sapiens", "rating": 4.9, "genre": "History"},
//         {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
//      {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
// ]
// ["Infinite Jest",  "The Catcher in the Rye", "Sapiens",  "A Brief History of Time",  "Clean Code"]

// function getTitles(books) {
//     let title = [];
//     for (let book of books) {
//         titles.push(book.title);
//         //console.log(titles)

//     }
//     return titles;
    
// }
// console.log(getTitles(books))
// ["Infinite Jest",  "The Catcher in the Rye"]
// function getTitles(books) {
//     let title=[];
//     for(let book of books){
//         if (book.genre="fiction"){
//         console.log(book.title)
//     }
//     }
//     return titles;
// }

//@@@@@@@@@@222 function of first class citizens

// function sayhello(){
//     return function (){
//         console.log("hello!👩‍🦲");
//     };
// }
// const result = sayhello();

// console.log(result,typeof result);

// result();
// function take function as argument greeting
//

//@@@@@@@@@@@@@@@@@@@@@@@@@ fun @@@@@@@@@@@@@@@ 
// Case 1:
// There no books which are >= 4.7
// The are no good books available 😔

// Case 2:
// There is only one
// Highest rated books is Sapiens

// Case 3:
// There are two more
// Highest rated books are: Sapiens, A Brief History of Time and Clean Code 
// Highest rated books are: Sapiens, A Brief History of Time and Clean Code 

// function getHightastRated(books) {
//     let Rated=[4.7];
//      for(let book of books)
//                 if (book.Rated="tecnology"){
//          console.log(book.Rated);
//      }
     
//      return Rated;
//     }
//     console.log 

//@@@@@@ higher interviews question @@@@@@@@@@@##########$$$$$$$$$$$$$$$
// curing
//parcel appllication
//scala
//sarp fish
//haskell
//point free
//@@@ optional changing @@@@@@@@@@2

// const csk1 = {
//   captain: "MSD",
//   color: "yellow",
//   stats: {
//     win: 5,
//     loss: 11,
//   },
// };

 //console.log(csk1.stats.win);

// const csk2 = {
//   captain: "MSD",
//   color: "yellow",
//   stats: {
//     // win: 5,
//     loss: 11,
//   },
// };

 //console.log(csk2.stats.win); // undefined

// const x = {};
// console.log(x.a); // undefined

// const csk3 = {
//   captain: "MSD",
//   color: "yellow",
// };

 //console.log(csk3.stats.win); // Cannot read properties of undefined (reading 'win')

// const csk4 = null;

// console.log(csk4.stats.win);
// Cannot read properties of null

// All cases we want the win
// Case 1: 5   Case 2,3 & 4 : 'Data not found'

// function getWinStat(team) {
//  if(!team.stats.win) {
//     return "data not found";
//    }

//     return team.stats.win;
// };
// console.log(csk2.stats.win);
// console.log(getWinStat(csk1)); // 5
// console.log(getWinStat(csk2)); // 'Data not found'
// console.log(getWinStat(csk3)); // 'Data not found'
// console.log(getWinStat(csk4)); // 'Data not found'

//const avengers = [
//   "Hulk",
//   "Iron man",
//   "Black widow",
//   "Captain america",
//   "Spider man",
//   "Thor",
// ];
//   const avenger = avengers.map((avengers) => avengers.length)
//   console.log(avenger)
// function getTitles(books){
// return books.map((book) => books.title)
// }
// console.log(books);
// 
//dribble.com developer 

