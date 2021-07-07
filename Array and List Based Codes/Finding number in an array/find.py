def find(A,num):
    for i in range(0,len(A)):
        if A[i]==num:
            return i
    return -1

a=[int(x) for x in input().strip().split()]
print(find(a,4))
