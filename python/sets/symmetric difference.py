#input
_=int(input())
m=input()
_=int(input())
n=input()

#splitting and mapping(string to int_list)
x=list(map(int,m.split()))
y=list(map(int,n.split()))

#creation of sets
a=set(x)
b=set(y)

result = list(a.union(b).difference(a.intersection(b)))

#sorting
result.sort()

#iteration
for i in range(len(result)):
    print(result[i])
