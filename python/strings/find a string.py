def count_substring(s, sub_string):
    count = 0
    l = len(sub_string)
    for i in range(len(s)-l+1):
        if s[i:i+l]==sub_string:
            count+=1
    return count

if __name__ == '__main__':