// 백준 제출 시, readFileSync('/dev/stdin') 으로 변경할 것
const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
    const people = input.map((person) => Number(person));
    const sum = people.reduce((acc, cur) => acc + cur, 0);

    for (let i = 0; i < people.length; i++) {
        for (let j = i + 1; j < people.length; j++) {
            if (sum - (people[i] + people[j]) === 100) {
                const result = people.filter((person, idx) => idx !== i && idx !== j);
                // 인덱스로 구현하든 값으로 구현하든 상관없음
                // const result = people.filter(
                //     (person) => person !== people[i] && person !== people[j]
                // );
                return result.sort((a, b) => a - b);
            }
        }
    }
}

const ans = solution(input); //함수 return으로 중첩for문 빠져나오거나 flag변수 추가해서 빠져나오거나
console.log(ans.join("\n"));
