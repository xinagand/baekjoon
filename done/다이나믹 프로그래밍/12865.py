# https://www.acmicpc.net/problem/12865 평범한 배낭

import sys
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

n, k = map(int, data[0].split())

items = []

for row in data[1:]:
    w, v = map(int, row.split())
    items.append([w, v])

dp = [0] * (k + 1)

for w, v in items:
    if w > k:
        continue
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i-w]+v, dp[i])

print(dp[k])
