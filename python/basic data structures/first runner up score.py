if __name__ == '__main__':
    #read the number of elements in the list
    n = int(input()) 

    #read the scores into a list
    l = list(map(int,input().strip().split()))[:n]

    #find the max score
    z = max(l)

    #remove the max score from the list, the second highest score is now the max score
    l = filter(lambda x: x!= z,l)
    
    
    print(max(l))
