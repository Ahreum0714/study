'use strict';

/**LECTURE: Functions */
function describeCountry(country, population, capitalCity) {
    return `${country} has ${population} million people and its capital city is ${capitalCity}`;
}

const korea = describeCountry('korea', 51, 'seoul');
const china = describeCountry('china', 100, 'beijing');
const japan = describeCountry('japan', 70, 'tokyo');

console.log(korea);
console.log(china);
console.log(japan);


/**LECTURE: Function Declarations vs. Expressions*/
const worldPopulation = 7900
const canada = 80;
const france = 30;
const usa = 1000;

// function declarations
function percentageOfWorld1(population) {
    return (population / worldPopulation) * 100;
}
const countryPopul1 = percentageOfWorld1(canada);
const countryPopul2 = percentageOfWorld1(france);
const countryPopul3 = percentageOfWorld1(usa);

console.log(countryPopul1);
console.log(countryPopul2);
console.log(countryPopul3);

// function expressions
const percentageOfWorld2 = function (population) {
    return (population / worldPopulation) * 100;
}
const popul1 = percentageOfWorld2(canada);
const popul2 = percentageOfWorld2(france);
const popul3 = percentageOfWorld2(usa);

console.log(popul1);
console.log(popul2);
console.log(popul3);


/**LECTURE: Arrow Functions */
const percentageOfWorld3 = population => (population / worldPopulation) * 100;


/** */