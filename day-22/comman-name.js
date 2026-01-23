
//     function task1(){
//     fetch(
//     "https://restcountries.com/v3.1/all?fields=name,flags,region,population,capital"
//     ).then((response) => response.json()) 
//      .then((data)=>(data))
//      .then((name) =>console.log(name.map((comman)=>comman?.name?.comman??"countryname is represent")));
// }
//     task1();
//    function task2(){
//     fetch(
//     "https://restcountries.com/v3.1/all?fields=name,flags,region,population,capital"
//     ).then((res)=> res.json())
//       .then((countries) =>
//       countries
//         .filter((country) => country.population >= 1_00_00_000)
//         .toSorted(
//           (countryA, countryB) => countryB.population - countryA.population,
//         )
//         .map((country) => country?.name?.common),
//     )
//     .then((result) => console.log(result));
// }
//  task2();

// function task3(){
    fetch(
    "https://restcountries.com/v3.1/all?fields=name,flags,region,population,capital"
    )
    .then((res)=> res.json())
    .then((data)=>data)
    .then((populations) =>
      populations
        .filter((country) => country.population >= 1_00_00_000)
        .toSorted(
          (countryA, countryB) => countryB.population - countryA.population)
         .map((country,ind)=console.log('${ind}.${countryname.comman} - ${countre.population}')
      ),    
        )    
// }
//    task3();


//    (countre,ind,) =>console.log('${ind}.${countre.name.comman} - ${countre.population})')
    //   ),
    
    
    
    
    
    
    
    
   