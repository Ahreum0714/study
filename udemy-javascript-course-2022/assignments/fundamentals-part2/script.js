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
const populations = [1441, 51, 880, 260];
console.log(populations.length === 4);

const percentages = [
    percentageOfWorld1(populations[0]),
    percentageOfWorld1(populations[1]),
    percentageOfWorld1(populations[2]),
    percentageOfWorld1(populations[3])
];
console.log(percentages);


/**LECTURE: Basic Array Operations (Methods)*/
const neighbours = ['china', 'japan', 'russia'];

neighbours.push('Utopia');
console.log(neighbours);

neighbours.pop();
console.log(neighbours);

if (!neighbours.includes('germany')) {
    console.log('Probably not a central European country :D');
}

neighbours[neighbours.indexOf('japan')] = 'Republic of Sweden';
console.log(neighbours);



/**LECTURE: Introduction to Objects */
const myCountry = {
    country: 'korea',
    capital: 'seoul',
    language: 'korean',
    population: 51,
    neighbours: ['china', 'japan', 'usa'],

    /**LECTURE: Object Methods */
    describe: function () {
        console.log(`${this.country} has ${this.population} million ${this.language}-speaking people,${this.neighbours.length} neighbouring countries and a capital called Helsinki.`);
    },

    checkIsland: function () {
        this.isIsland = (this.neighbours.length === 0) ? true : false;
    }
}



/**LECTURE: Dot vs. Bracket Notation */
console.log(`${myCountry.country} has ${myCountry.population} million ${myCountry.language}-speaking people,${myCountry.neighbours.length} neighbouring countries and a capital called Helsinki.`);

myCountry.population += 2;
console.log(`${myCountry.country} has ${myCountry.population} million ${myCountry.language}-speaking people,${myCountry.neighbours.length} neighbouring countries and a capital called Helsinki.`);

myCountry['population'] -= 2;
console.log(`${myCountry.country} has ${myCountry.population} million ${myCountry.language}-speaking people,${myCountry.neighbours.length} neighbouring countries and a capital called Helsinki.`);



/**LECTURE: Object Methods */
myCountry.describe();
myCountry.checkIsland();
console.log(myCountry);



/**LECTURE: Iteration: The for Loop */

for (let i = 1; i <= 50; i++) {
    console.log(`Voter number ${i} is currently voting`);
}



/**LECTURE: Looping Arrays, Breaking and Continuing */



/**LECTURE: Looping Backwards and Loops in Loops */




/**LECTURE: The while Loop */




/** */