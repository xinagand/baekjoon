# https://www.acmicpc.net/problem/1934 최소공배수
# 최대공약수. gcd, lcm은 math에 있다. 개쩌는 거니 무조건 암기.

from math import lcm
import sys
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

N = int(data[0])
for i in range(1, N+1):
    a, b = map(int, data[i].split())
    print(lcm(a, b))
