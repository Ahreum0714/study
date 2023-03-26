# https://www.acmicpc.net/problem/1062 가르침 (3840ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
words = [set(input().rstrip()[4:-4]) for _ in range(n)]
readable = ['a','n','t','i','c']
learn = [False] * 26
ans = 0

if k < len(readable):
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

# 필수 알파벳
for c in readable:
    learn[ord(c) - ord('a')] = True

# DFS로 최대개수 탐색
def countReadableWords(i, cnt):
    global ans
    
    if cnt == k-5:
        read_cnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                read_cnt += 1
        ans = max(ans, read_cnt)
        return
    
    for i in range(i, 26):
        if not learn[i]:
            learn[i] = True
            countReadableWords(i, cnt+1)
            learn[i] = False

countReadableWords(0, 0)
print(ans)

'''
### DFS 말고 combinations&브루트포스 풀이법도 있음 (3276ms)

n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함

first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def countReadableWords(data, learned):
   cnt = 0
   for word in data:
      canRead = 1
      for w in word:
          # 안배웠으니까 못읽는다.
         if learned[ord(w)] == 0:
            canRead = 0
            break
      if canRead == 1:
         cnt += 1
   return cnt

if k >= 5:
   learned = [0] * 123
   for x in first_word:
      learned[ord(x)] = 1

   # 남은 알파벳 중에서 k-5개를 선택해본다.
   for teach in list(combinations(remain_alphabet, k-5)):
      for t in teach:
         learned[ord(t)] = 1
      cnt = countReadableWords(data, learned)

      if cnt > answer:
         answer = cnt
      for t in teach:
         learned[ord(t)] = 0
   print(answer)
else:
   print(0)
'''