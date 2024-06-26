/*
Everything in between is a comment.
*/

let myAge = 21;  // `var`was used earlier, is not used anymore
const myName = "Bob";  // must be initialized on declaration
/*
`Constant` actually means, that the pointer to the object cannot change. So only constants of immutable types cannot change, constants of mutable types can!
Mutable types are complex and sequential types, immutable types are the simple types.
*/
let isAlive = true

console.log("-----  IF STATEMENT")
if (myName === "Bob") {
    console.log("Yes")
} else {
    console.log("No")
}

console.log("-----  FUNCTION")
function logName(name) {
    console.log(`Hello ${name}`);  // Attention: Backticks!
}
logName(myName);

console.log("-----  ARRAYS")
let myNameArray = ["Chris", "Bob", "Jim"];
let myNumberArray = [10, 15, 40];
console.log(myNameArray[1]);
const random = ['tree', 795, [0, 1, 2]];
console.log(random.length)

console.log("-----  OBJECTS")
let dog = { name: "Spot", breed: "Dalmatian" };
console.log(dog.name);

console.log(typeof isAlive);


console.log("-----  FOR LOOPS")
for (const name of myNameArray) {
    console.log(name);
}

for (let i = 0; i < myNameArray.length; i++) {
    console.log(myNameArray[i]);
}