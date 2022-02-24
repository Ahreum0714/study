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
