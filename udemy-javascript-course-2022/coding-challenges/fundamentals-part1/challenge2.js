// Coding Challenge #2
// Use the BMI example from Challenge #1, and the code you already wrote, and
// improve it.
// Your tasks:
// 1. Print a nice output to the console, saying who has the higher BMI. The message
// is either "Mark's BMI is higher than John's!" or "John's BMI is higher than Mark's!"
// 2. Use a template literal to include the BMI values in the outputs. Example: "Mark's
// BMI (28.3) is higher than John's (23.9)!"
// Hint: Use an if/else statement 😉

const markMass = 95;
const markHeight = 1.88;
const johnMass = 85;
const johnHeight = 1.76;

const BMImark = markMass / markHeight ** 2;
const BMIjohn = johnMass / johnHeight ** 2;
let markHigherBMI = BMImark > BMIjohn;

console.log(BMImark, BMIjohn, markHigherBMI);

if (BMIjohn > BMImark) {
    console.log(`John's BMI(${BMIjohn}) is higher than Mark's BMI(${BMImark})!`);
} else {
    console.log(`Mark's BMI(${BMImark}) is higher than John's (${BMIjohn})`);
}