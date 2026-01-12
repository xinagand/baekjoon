# https://www.acmicpc.net/problem/1002 터렛
# 기하학, 조건처리

from math import sqrt
import sys
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

n = int(data[0])

for row in data[1:]:
    x1, y1, r1, x2, y2, r2 = map(int, row.split())
    if (x1, y1) == (x2, y2):
        if r1==r2:
            print(-1)
        else:
            print(0)
        continue
    else:
        dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if dist == r1+r2:
            print(1)
        elif dist < r1+r2:
            if max(r1, r2) == min(r1, r2) + dist:
                print(1)
            elif max(r1, r2) > min(r1, r2) + dist:
                print(0)
            else:
                print(2)
        else:
            print(0) 
            
            
# GPT
# 논리는 같지만, 중복제거와 함수사용

import sys
from math import isclose

sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

n = int(data[0])

for row in data[1:]:
    x1, y1, r1, x2, y2, r2 = map(int, row.split())

    # 중심이 같은 경우
    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)  # 무한대의 교점
        else:
            print(0)   # 중심은 같지만 반지름이 다른 경우
        continue
    
    # 두 중심 사이의 거리의 제곱 계산
    dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    r_sum_sq = (r1 + r2) ** 2
    r_diff_sq = (r1 - r2) ** 2

    # 원이 외접하는 경우
    if isclose(dist_sq, r_sum_sq):
        print(1)
    # 원이 내접하는 경우
    elif isclose(dist_sq, r_diff_sq):
        print(1)
    # 두 원이 겹치는 경우 (교점이 두 개)
    elif r_diff_sq < dist_sq < r_sum_sq:
        print(2)
    # 두 원이 겹치지 않는 경우 (서로 떨어져 있는 경우)
    else:
        print(0)