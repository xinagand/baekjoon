# https://level.goorm.io/exam/223334/토지-판매/quiz/1

import sys
sys.setrecursionlimit(10**6)

# input 
input = """3 4 2
1 2 2 3
2
1 1 3 3
2 2 3 4
"""  
# input = sys.stdin.read().strip().splitlines()
data = input.strip().splitlines()  

N, M, B = map(int, data[0].split())
p, q, r, s = map(int, data[1].split())
K = int(data[2])

def trans(n, B):
	result = []
	while n:
		m, a = divmod(n, B)
		result.append(a)
		n = m
	return ''.join(map(str, result[::-1]))

def add_pos(a, b):
    maxlen = max(len(a), len(b)) 
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    out = []
    for i in range(maxlen):
        add = (int(a[i]) + int(b[i])) % B
        out.append(str(add))
    return ''.join(out)

def price(a, b):
    a = p*a + q
    b = r*b + s
    
    str_a = trans(a, B)
    str_b = trans(b, B)
    
    return add_pos(str_a, str_b)
    
# Precompute the prices for all positions to speed up queries
prices = [[price(i, j) for j in range(M + 1)] for i in range(N + 1)]
print(prices)

orders = [list(map(int, x.split(' '))) for x in data[3:]]

def add_sum(lst):
    maxlen = max([len(x) for x in lst]) 
    lst =[x.zfill(maxlen) for x in lst]
    
    out = []
    for i in range(maxlen):
        add = (sum([int(x) for x in lst])) % B
        out.append(str(add))
    return ''.join(out)

for order in orders:
    x1, y1, x2, y2 = order
    lst = []
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            print(j, i)
            lst.append(prices[j][i])
    print(add_sum(lst))
