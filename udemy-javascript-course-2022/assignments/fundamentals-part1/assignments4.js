/* Lecture: Basic Operators */

// 1. If your country split in half, and each half would contain half the population,
// then how many people would live in each half?
// 2. Increase the population of your country by 1 and log the result to the console
// 3. Finland has a population of 6 million. Does your country have more people than
// Finland?
// 4. The average population of a country is 33 million people. Does your country
// have less people than the average country?
// 5. Based on the variables you created, create a new variable 'description'
// which contains a string with this format: 'Portugal is in Europe, and its 11 million
// people speak portuguese'
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
