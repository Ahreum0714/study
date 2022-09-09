// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
// https://www.acmicpc.net/problem/3085 사탕 게임 (440ms)
const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const n = Number(input[0]);
const candy = new Array(n).fill([]);
for (let i = 0; i < n; i++) {
    tmp = [];
    for (let j = 0; j < n; j++) {
        tmp.push(input[i + 1][j]);
    }
    candy[i] = tmp;
}
let ans = 1;

// 사탕을 먹을 수 있는 최대 개수 카운트 함수
function countCandy() {
    // 행
    for (let i = 0; i < n; i++) {
        let cnt = 1;
        for (let j = 0; j < n - 1; j++) {
            if (candy[i][j] == candy[i][j + 1]) {
                cnt++;
                ans = Math.max(ans, cnt);
            } else {
                cnt = 1;
            }
        }
    }
    // 열
    for (let i = 0; i < n; i++) {
        let cnt = 1;
        for (let j = 0; j < n - 1; j++) {
            if (candy[j][i] == candy[j + 1][i]) {
                cnt++;
                ans = Math.max(ans, cnt);
            } else {
                cnt = 1;
            }
        }
    }
}

function swapCandy(i, j, flag) {
    if (flag == true) {
        // 가로 바꾸기 (열의 원소 바꾸기)
        const tmp = candy[i][j];
        candy[i][j] = candy[i][j + 1];
        candy[i][j + 1] = tmp;
    } else {
        // 세로 바꾸기 (행의 원소 바꾸기)
        const tmp = candy[j][i];
        candy[j][i] = candy[j + 1][i];
        candy[j + 1][i] = tmp;
    }
}

// [모든 인접한 두 자리 바꾸면서 최대 개수 찾기]
// 가로 바꾸기 (열의 원소 바꾸기)
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - 1; j++) {
        swapCandy(i, j, true); // 바꾸기
        countCandy();
        swapCandy(i, j, true); // 원위치
    }
}
// 세로 바꾸기 (행의 원소 바꾸기)
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - 1; j++) {
        swapCandy(i, j, false); // 바꾸기
        countCandy();
        swapCandy(i, j, false); // 원위치
    }
}

console.log(ans);
