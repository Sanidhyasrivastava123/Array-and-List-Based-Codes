def finder(A,B):
    result=0
    #use XOR method between the elements in Array

    for num in A+B:
        result^=num
        

    return result

A= [int(x) for x in input().strip().split()]
B= [int(x) for x in input().strip().split()]
print(finder(A,B))
