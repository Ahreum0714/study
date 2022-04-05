// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");

const n = Number(input[0]);
let answer = "";

for (let i = 1; i <= n; i++) {
  answer += i + "\n";
}

// for 문 안에서 바로 console.log해줄 경우 시간 초과 됨!
console.log(answer);
