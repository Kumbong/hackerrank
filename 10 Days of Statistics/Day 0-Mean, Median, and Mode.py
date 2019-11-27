# Enter your code here. Read input from STDIN. Print output to STDOUT

import statistics as st


size = int(input())
data = list(map(int, input().split()))


def getMode(list):
    mode = 0
    size = len(list)
    count, max = 0, 0
    copy = list
    copy.sort()
    current = 0
    for i in copy:
        if (i == current):
            count += 1
        else:
            count = 1
            current = i
        if (count > max):
            max = count
            mode = i
    return mode


print("%.1f"%(float(st.mean(data))))
print("%.1f"%(float(st.median(data))))

print(getMode(data))
