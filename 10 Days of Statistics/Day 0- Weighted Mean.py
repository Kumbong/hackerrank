# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())

dataset = list(map(int, input().split()))

data_loc = list(map(int , input().split()))

weighted = []

weight = 0

for i in range(len(dataset)):
    weight = dataset[i] * data_loc[i]  
    weighted.append(weight)

weighted_sum = float(sum(weighted)/ sum(data_loc))

print("%.1f"%(weighted_sum))
