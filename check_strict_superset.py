# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int, input().split()))
n = int(input())
sets = []

for _ in range(n):
    sets.append(set(map(int, input().split())))
    
result = True

for s in sets:
    if not (setA.issuperset(s) and len(setA - s) != 0):
        result = False
print(result) 
