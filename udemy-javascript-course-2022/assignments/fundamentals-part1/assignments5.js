/* Lecture: Strings and Template Literals */

// 1. Recreate the 'description' variable from the last assignment, this time
// using the template literal syntax

let country = 'korea';
let continent = 'asia';
const motherLanguage = 'Korean';
let koreaPopulation = 51;

//1
console.log(koreaPopulation / 2);
//2
koreaPopulation++;
console.log(koreaPopulation);
//3
let finlandPopulation = 6;
let isLarger = koreaPopulation > finlandPopulation;
console.log(isLarger);
//4
let averagePopulation = 33;
let isLesser = koreaPopulation < averagePopulation;
console.log(isLesser);
//5
let description = country + ' is in ' + continent + ', and its ' + koreaPopulation + ' million people speak ' + motherLanguage;
console.log(description);

description = `${country} is in ${continent}, and its ${koreaPopulation} million people speak ${motherLanguage}`;
console.log(description);