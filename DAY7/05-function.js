//why we need function
// for reuse, update data on one  place 
// Declaration,
// call
//parameter, argument , 

// function moodReport(m1 = `😊` ,m2 = `morning 🌄`) {
//     return `feeling ${m1} this ${m2}`
// } 

// console.log(moodReport());
// console.log(moodReport("😎", "afternoon ☀️"));




// console.log(checkAgeCategory());
// console.log(checkAgeCategory(12));
// console.log(checkAgeCategory(65));

// const wizard = { name: "Merlin", title: "Archmage", wand: { core: "Phoenix Feather" } };
// console.log(introduceWizard(wizard));

// function introduceWizard(wiz){
//     return `${wiz.title} + ${wiz.name} + ${wiz.wand.core} core`
// }
// console.log(introduceWizard());


//  mergeInventory(existing,incoming);
// const shelf = ["🍎", "🥪"];
// const delivery = ["🍫", "🍇"];
// console.log(mergeInventory(shelf, delivery));
// ["🍎","🥪","🍫","🍇","🧃"];

// const shelf = ["🍎", "🥪"];
// const delivery = ["🍫", "🍇"];

// function mergeInventory(existing,incoming){
//     return `[...existing , ...incoming, "🧃"]`;
// }
// console.log(mergeInventory(shelf,delivery));


// console.log(packBag("Natasha", "💄", "🔫"));
// console.log(packBag());
// 🎒 Natasha's bag contains: 💄, 🔫
// 🎒 Anon's bag is empty.

// function packBag(name = "Anon", ...items) {
//   if (items.length === 0) {
//     return `🎒 ${name}'s bag is empty.`;
//   }
//   return `🎒 ${name}'s bag contains: ${items.join(", ")}`;
// }

// console.log(packBag("Natasha", "💄", "🔫"));
// // 🎒 Natasha's bag contains: 💄, 🔫

// console.log(packBag());
// // 🎒 Anon's bag is empty.

// console.log(whereAreYou({ user: "Thor", location: { city: "Asgard", planet: "Yggdrasil" } }));
// console.log(whereAreYou({}));
// Thor is currently in Asgard, Yggdrasil 🌍
// Someone is currently in Unknown, Earth 🌍

function whereAreYou(personObj) {
    const{ user ="someone",
 location = {} } = personObj;
   const{ city = "Unknown" ,
    planet ="Earth" } = 
    location;

    return `${user} iscurrentaly in ${city},${planet}🌍`;
   }
   console.log(whereAreYou({ user: "Thor", location: { city: "Asgard", planet: "Yggdrasil" } }));
//    Thor is currently in Asgard, Yggdrasil 🌍
    console.log(whereAreYou({}));
    // Someone is currently in Unknown, Earth 🌍

