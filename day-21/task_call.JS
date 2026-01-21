function promise1() {
    return new promise((resolve, reject)=> {
     setTimeout(()=>{
        console.log("hi 1");
        resolve();
     },1000);
    });
    
}
function promise2 () {
    return new promise((resolve, reject)=> {
     setTimeout(()=>{
        console.log("hi 2");
        resolve();
     },1000);
    });
    
}
function promise3 () {
    return new promise((resolve, reject)=> {
     setTimeout(()=>{
        console.log("hi 3");
        resolve();
     },1000);
    });
    
}
function promise4 () {
    return new promise((resolve, reject)=> {
     setTimeout(()=>{
        console.log("hi 4");
        resolve();
     },1000);
    });
    
}
function promise5 () {
    return new promise((resolve, reject)=> {
     setTimeout(()=>{
        console.log("hi 5");
        resolve();
     },1000);
    });
    
}
promise1()
 .then(()=>promise2())
 .then(()=>promise3())
 .then(()=>promise4())
 .then(()=>promise5())
 .then(()=>{
    console.log("happy pongal");
 })
 .catch((good)=>{
    console.log("yah:",good)
 });





// let countdown = 5;

//       setTimeout(() => {
//         document.querySelector("h1").innerText = --countdown;
//         setTimeout(() => {
//           document.querySelector("h1").innerText = --countdown;
//           setTimeout(() => {
//             document.querySelector("h1").innerText = --countdown;
//             setTimeout(() => {
//               document.querySelector("h1").innerText = --countdown;
//               setTimeout(() => {
//                 document.querySelector("h1").innerText = "Happy Pongal 🌾";
//               }, 1000);
//             }, 1000);
//           }, 1000);
//         }, 1000);
//       }, 1000);