# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = list(map(int, input().split()))
d= defaultdict(list)

for _ in range(n):
    d['n'].append(input())

for _ in range(m):
    d['m'].append(input())
    
    
for i in d['m']:
    appear = False
    for j, letter in enumerate(d['n']):
        if i == letter:
            appear = True
            print(j + 1, end=" ")
    if not appear:
        print(-1, end=' ')
    print()
