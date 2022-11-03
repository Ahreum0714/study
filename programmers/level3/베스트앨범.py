# [Prog] 해시 - lv3: 베스트앨범  https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    song = {}          # 장르별 재생 노래 {genre: (idx, play)}
    song_total = {}     # 장르별 총 재생 횟수 {genre: total}
    
    # 장르별 총 재생 횟수 및 장르 노래 dictionary 만들기
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in song:
            song[genre] = [(idx, play)]
        else:
            song[genre].append((idx, play))
        
        if genre not in song_total:
            song_total[genre] = play
        else:
            song_total[genre] += play
            
    # 1. 장르별 재생 횟수 내림차순 정렬
    for (genre, total) in sorted(song_total.items(), key=lambda x:x[1], reverse=True):
        # 2. 장르 내에서 가장 많이 재생된 노래 두 개씩 모아 베스트 앨범에 수록
        for (idx, play) in sorted(song[genre], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
