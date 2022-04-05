// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");

const words = input[0];
let oneLine = "";

for (let i = 0; i < words.length; i++) {
  oneLine += words[i];
  if (oneLine.length === 10) {
    console.log(oneLine);
    oneLine = "";
  } else if (i === words.length - 1) console.log(oneLine);
}

// slice랑 substring 생각을 왜 못했을까...!

// 방법 1
// while (input.length > 0) {
//   console.log(input.slice(0, 10));
//   input = input.slice(10);
// }

// 방법 2
// for(let i = 0; i < input.length; i += 10) {
//     console.log(input.substring(i,i+10));
// }
