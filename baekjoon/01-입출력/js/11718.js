// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");

for (let i = 0; i < input.length; i++) {
  console.log(input[i]);
}
