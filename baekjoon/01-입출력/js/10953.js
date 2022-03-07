// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");
let num = input[0];
for (let i = 1; i <= num; i++) {
  let column = input[i].split(",");
  console.log(parseInt(column[0]) + parseInt(column[1]));
}
