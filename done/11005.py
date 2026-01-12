# https://www.acmicpc.net/problem/11005 진법 변환 2

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

conv = {**{i:str(i) for i in range(10)}, **{i-55:chr(i) for i in range(65, 91)}}

def trans(data):
    n, k = map(int, data.split())
    result = deque()
    
    while n > 0:
        m = n % k
        result.appendleft(conv[m])
        n //= k    
    return ''.join(result)

print(trans(data[0]))