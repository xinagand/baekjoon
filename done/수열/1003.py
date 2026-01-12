# https://www.acmicpc.net/problem/1003 피보나치 함수
# 수열

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

numbers = list(map(int, INPUT[1:]))

COUNT = [[0, 0] for _ in range(41)]
COUNT[0] = [1, 0]
COUNT[1] = [0, 1]
COUNT[2] = [1, 1]

for i in range(2, max(numbers)+1):
    C0 = COUNT[i-1][0] + COUNT[i-2][0]
    C1 = COUNT[i-1][1] + COUNT[i-2][1]
    COUNT[i] = [C0, C1]

for num in numbers:
    print(COUNT[num][0], COUNT[num][1])