/* Lecture: Type Conversion and Coercion */

// 1. Predict the result of these 5 operations without executing them:
// '9' - '5';
// '19' - '13' + '17';
// '19' - '13' + 17;
// '123' < 57;
// 5 + 6 + '4' + 9 - 4 - 2;
// 2. Execute the operations to check if you were righ

console.log('9' - '5'); // 4 (number)
console.log('19' - '13' + '17'); // 617 (string)
console.log('19' - '13' + 17); // 23 (number)
console.log('123' < 57); // false
console.log(5 + 6 + '4' + 9 - 4 - 2); // 1143 (number)