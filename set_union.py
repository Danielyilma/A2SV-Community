# Enter your code here. Read input from STDIN. Print output to STDOUT
no_english = int(input())
english_sub = set(map(int, input().split()))
no_french = int(input())
french_sub = set(map(int, input().split()))

print(len(english_sub + french_sub))
