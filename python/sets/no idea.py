# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()

arr = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in arr]))
