const fs = require("fs")
const input = fs.readFileSync('/dev/stdin').toString().split("\n")
const n = Number(input[0])
const seq = input[1].split(" ").map(Number)

let dp = new Array(n).fill(-1000)
dp[0] = seq[0]
for (let i = 1; i < n; i++) {
  dp[i] = Math.max(dp[i-1] + seq[i], seq[i])
}

console.log(Math.max(...dp))
