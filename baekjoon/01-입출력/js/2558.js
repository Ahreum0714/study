// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const [a, b] = fs.readFileSync("예제.txt").toString().split("\n").map(Number);

console.log(a + b);
