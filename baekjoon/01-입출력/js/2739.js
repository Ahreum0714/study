// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");

const n = parseInt(input[0]);

let result = "";

for (let i = 1; i <= 9; i++) {
  result += `${n} * ${i} = ${n * i}\n`;
}

console.log(result);
