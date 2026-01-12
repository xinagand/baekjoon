# https://www.acmicpc.net/problem/2533 사회망 서비스(SNS)
# 다이나믹 프로그래밍, 트리
# 타임아웃...

from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

N = int(data[0])

tree = defaultdict(list)
for row in data[1:]:
    a, b = map(int, row.split())
    tree[a] = tree[a] + [b]
    tree[b] = tree[b] + [a]

visited = [False] * (N+1)
# 재귀를 사용한 DFS 함수
def dfs(current):
    if not visited[current]:
        visited[current] = True
        for neighbor in tree[current]:
            dfs(neighbor)      

order = dfs(1, list())

colored = set()

while order:
    i = order.pop()
    if i in colored:
        continue
    for n in tree[i]:
        if n in order:
            if n not in colored:
                colored.add(n)
print(len(colored))

# GPT 코드
# dfs기반한 서치방법

from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')
input = sys.stdin.read()
data = input.splitlines()

N = int(data[0])

tree = defaultdict(list)

for row in data[1:]:
    a, b = map(int, row.split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(current):
    visited[current] = True
    dp[current][0] = 0
    dp[current][1] = 1
    
    for c in tree[current]:
        if not visited[c]:
            dfs(c)
            dp[current][0] += dp[c][1]
            dp[current][1] += min(dp[c][0], dp[c][1])
            
dfs(1)
print(min(dp[1][0], dp[1][1]))