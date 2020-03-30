# Enter your code here. Read input from STDIN. Print output to STDOUT

n  = int(input())
stack = []

for i in range(n):
    x = [int(i) for i in input().split(' ')]
 
    if x[0]==1:
        if stack:
            m = max(stack[-1],x[1])
            stack.append(m)
        else:
            stack.append(x[1])
    elif x[0]==2:
        stack.pop()
    elif x[0]==3:
        print(stack[-1])
