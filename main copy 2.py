# https://www.acmicpc.net/problem/2559 수열
# 누적합, 투포인터, 슬라이딩 윈도우


import sys
sys.setrecursionlimit(10**6)

# input 
input = """10 2
3 -2 -4 -9 0 3 7 13 8 -3"""  
# input = sys.stdin.read().strip().splitlines()

data = input.strip().splitlines()  

# code
n, k = map(int, data[0].split())
nums = list(map(int, data[1].split()))
    
pack = [nums[i:n-k+i+1] for i in range(k)]
dp = [sum(x) for x in zip(*pack)]
print(dp)


# 짧지만 메모리 터지는코드
import sys
sys.setrecursionlimit(10**6)

# input 
input = """10 2
3 -2 -4 -9 0 3 7 13 8 -3"""  
# input = sys.stdin.read().strip().splitlines()

data = input.strip().splitlines()  

# code
n, k = map(int, data[0].split())
nums = list(map(int, data[1].split()))
    
pack = [nums[i:n-k+i+1] for i in range(k)]
dp = [sum(x) for x in zip(*pack)]
print(dp)
    