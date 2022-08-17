def solution(board, moves):
    answer = 0
    bucket = [0]

    for x in moves:
        for y in range(len(board)):
            if board[y][x-1] > 0:  # 인형뽑기
                bucket.append(board[y][x-1])
                board[y][x-1] = 0                
               
                if bucket[-1] == bucket[-2]: # 터트리기
                    bucket.pop()
                    bucket.pop()
                    answer += 2
                break
    return answer

ans = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(ans)