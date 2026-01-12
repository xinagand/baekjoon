# 

import sys
sys.setrecursionlimit(10**6)

# input 
input = """7
1 1 3 4 2 1 7"""  
# input = sys.stdin.read().strip().splitlines()

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))

h = 2
while h < N:
	h *= 2

sgt = [0] * (h*2)

for i, v in enumerate(prices):
	sgt[h+i] = v

def get_max(i):
	left = sgt[i * 2]
	right = sgt[i * 2 + 1]
	return max(left, right)

for i in range(h-1, 0, -1):
	sgt[i] = get_max(i)
print(sgt)

# 특정 인덱스 이전 구간에서 최대값 찾기 (리프 노드 기준)
def find_max(right):
	right = h + right  # 리프 노드의 실제 인덱스로 변환
	max_val = float('-inf')  # 최대값을 저장할 변수 초기화

	# 구간 [0, right]의 최대값 찾기
	while right > 1:
			if right % 2 == 1:  # right가 홀수인 경우, 현재 노드를 포함
					max_val = max(max_val, sgt[right - 1])
			right //= 2  # 부모 노드로 이동

	return max_val

# # --- 값을 키로, 키 이하 합산중 최대를 딕셔너리로 저장. 13부터 타임아웃. 틀린건 없음
from collections import defaultdict
import heapq

best_dict = defaultdict(int)

for i, v in enumerate(prices):
	prev_best = best_dict[find_max(v-1)]
	best_dict[v] = prev_best + v
	print(f"0-{i}: best[{prev_best}]")

		
print(best_dict)