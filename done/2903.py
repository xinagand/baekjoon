# https://www.acmicpc.net/problem/2903 중앙 이동 알고리즘

import sys
sys.stdin = open('input.txt')

dots = 2 ** int(input()) + 1
print(f"{dots**2:.0f}")