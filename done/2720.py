# https://www.acmicpc.net/problem/2720 세탁소 사장 동혁

import sys
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

size = [25, 10, 5, 1]

for row in data[1:]:
    coins = []
    change = float(row)
    
    for c in size:
        add, left = divmod(change, c)
        coins.append(str(int(add)))
        change = left
    print(' '.join(coins))
            