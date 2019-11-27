# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from statistics import mean

size = int(input())

dataset = list(map(int, input().split()))
def stdev(dataset):
    n = len(dataset)
    mean_of_data = mean(dataset)
    num = 0
    for element in dataset:
        sub_square = ( element - mean_of_data ) ** 2
        num += sub_square
    return math.sqrt(num/n)


print("%.1f"%(stdev(dataset)))


