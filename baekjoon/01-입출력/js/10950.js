// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");
const num = parseInt(input[0]);
for (let i = 0; i < num; i++) {
  let column = input[i + 1].split(" ");
  console.log(parseInt(column[0]) + parseInt(column[1]));
}
