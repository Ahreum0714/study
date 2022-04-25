// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().split("\n");

const n = input[0];
let dp = new Array(1000001);

dp[1] = 0;
for (let i = 2; i <= n; i++) {
  dp[i] = dp[i - 1] + 1;
  if (i % 3 === 0) dp[i] = Math.min(dp[i / 3] + 1, dp[i]);
  if (i % 2 === 0) dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
}

console.log(dp[n]);
