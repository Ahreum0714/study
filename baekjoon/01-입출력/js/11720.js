// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");

const n = input[0];
const numbers = input[1];

let sum = 0;
for (let i of numbers) {
  sum += Number(i);
}

console.log(sum);
