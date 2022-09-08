// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
let dp = new Array(n).fill(1);

for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
        if (arr[i] > arr[j]) {
            dp[i] = Math.max(dp[i], dp[j] + 1);
        }
    }
}

console.log(Math.max(...dp));
