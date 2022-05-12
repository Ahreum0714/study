// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split(" ").map(Number);
// 숫자로 형변환 필수!!!!!! 안그러면 문자열로 아니까 재대로 덧셈 안됨
let x = input[0];
let y = input[1];
let totalDays = 0;
const days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

for (let i = 0; i < x - 1; i++) {
  totalDays += days[i];
}
totalDays += y;

const k = totalDays % 7;
switch (k) {
  case 0:
    console.log("SUN");
    break;
  case 1:
    console.log("MON");
    break;
  case 2:
    console.log("TUE");
    break;
  case 3:
    console.log("WED");
    break;
  case 4:
    console.log("THU");
    break;
  case 5:
    console.log("FRI");
    break;
  case 6:
    console.log("SAT");
    break;
  default:
    break;
}
