# https://www.acmicpc.net/problem/1654 랜선 자르기
# 이진탐색

import sys
sys.stdin = open('input.txt')

IN = sys.stdin.read()
data = IN.splitlines()

N, K = data[0].split()
lines = list(map(int, data[1:]))

CAN = sum(lines) / int(K)

while True:
    SUM = [x // CAN for x in lines]
    if sum(SUM) >= int(K):
        break
    print("CAN", CAN, "SUM", SUM)
    next = [x / (y+1) for x, y in zip(lines, SUM)]
    CAN = int(max(next))
    
print(int(CAN))


# GPT 답변
# 생각해보면, 어차피 자르는 기준은 1~가장긴길이 사이에서의 탐색임. 이제 이 탐색을 얼마나 빠르게할지가 관건?

import sys
sys.stdin = open('input.txt')

IN = sys.stdin.read()
data = IN.splitlines()

N, K = map(int, data[0].split())
lines = list(map(int, data[1:]))

start, end = 1, max(lines)

result = 0
while start <= end:
    mid = (start + end) // 2
    count = sum(line // mid for line in lines)
    
    if count >= K:
        result = mid
        start = mid + 1 
    else:
        end = mid - 1

print(result)
