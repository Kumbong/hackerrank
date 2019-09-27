if __name__ == '__main__':
    nested_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,score])
    
    nested_list.sort(key=lambda x: (x[1],x[0]))

    m = nested_list[0][1]

    nested_list = list(filter(lambda x: x[1]!=m,nested_list))

    m = nested_list[0][1]

    res = list(filter(lambda x: x[1]==m,nested_list))

    for el in res:
        print(el[0])

    

