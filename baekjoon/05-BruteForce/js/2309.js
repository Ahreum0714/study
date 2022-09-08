// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().split("\n");

const people = input.map((person) => Number(person));
const sum = people.reduce((acc, cur) => acc + cur, 0);

outer_loop: for (let i = 0; i < people.length; i++) {
    for (let j = i + 1; j < people.length; j++) {
        if (sum - (people[i] + people[j]) === 100) {
            ans = people.filter((person) => person != people[i] && person != people[j]);
            ans.sort((a, b) => a - b); // 숫자 오름차순 정렬
            ans.forEach((person) => console.log(person));
            break outer_loop;
        }
    }
}
