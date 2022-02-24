'use strict';

/**LECTURE: Functions */
function describeCountry(country, population, capitalCity) {
    return `${country} has ${population} million people and its capital city is ${capitalCity}.`;
}

const descKorea = describeCountry('Korea', 51, 'seoul');
const descChina = describeCountry('China', 100, 'beijing');
const descJapan = describeCountry('Japan', 70, 'tokyo');
console.log(descKorea, descChina, descJapan);



/**LECTURE: Function Declarations vs. Expressions*/
const worldPopulation = 7900

// function declarations //
function percentageOfWorld1(population) {
    return (population / worldPopulation) * 100;
}

const perc1 = percentageOfWorld1(80);
const perc2 = percentageOfWorld1(30);
const perc3 = percentageOfWorld1(1000);
console.log(perc1, perc2, perc3);

// function expressions //
const percentageOfWorld2 = function (population) {
    return (population / worldPopulation) * 100;
}

const popul1 = percentageOfWorld2(80);
const popul2 = percentageOfWorld2(30);
const popul3 = percentageOfWorld2(1000);
console.log(popul1, popul2, popul3);



/**LECTURE: Arrow Functions */
const percentageOfWorld3 = population => (population / worldPopulation) * 100;

const percPortugal = percentageOfWorld3(10);
const percChina = percentageOfWorld3(1441);
const percUSA = percentageOfWorld3(332);
console.log(percPortugal, percChina, percUSA);


/**LECTURE: Functions Calling Other Functions */
function describePopulation(country, population) {
    const percentage = percentageOfWorld1(population);
    const description = `${country} has ${population} million people, which is about ${percentage} of the world.`;
    console.log(description);
}
describePopulation('China', 1441);
describePopulation('USA', 332);
describePopulation('Portugal', 10);



/**LECTURE: Introduction to Arrays */




/**LECTURE: Basic Array Operations (Methods)*/




/**LECTURE: Introduction to Objects */




/**LECTURE: Dot vs. Bracket Notation */