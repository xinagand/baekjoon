# https://www.acmicpc.net/problem/10844 쉬운 계단 수 

import sys
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

dp = [0] + [1] * 9
for i in range(1, int(data[0])):
    old_dp = dp.copy()
    for j in range(1, 9):
        dp[j] = old_dp[j-1] + old_dp[j+1]
    dp[0] = old_dp[1]
    dp[9] = old_dp[8]
    print(i, dp)
print(sum(dp) % 1000000000)