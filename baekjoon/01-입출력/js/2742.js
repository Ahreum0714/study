// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString();

const n = Number(input);
let answer = "";

for (let i = n; i > 0; i--) {
  answer += i + "\n";
}

console.log(answer);
