def finder(A,B):
    A.sort()
    B.sort()
    for num1,num2 in zip(A,B):
        if num1 !=num2:
            return num1
    return A[-1]

A= [int(x) for x in input().strip().split()]
B= [int(x) for x in input().strip().split()]
print(finder(A,B))
