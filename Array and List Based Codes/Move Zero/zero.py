def movezero(A):
    j=0
    for i in A:
        if(i!=0):
            A[j]=i
            j+=1
    for x in range(j,len(A)):
        A[x]=0

    print(A)

A=[int(x) for x in input().strip().split()]
movezero(A)
