def maxproduct(A):
    maxproduct=0
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i]*A[j]>=maxproduct:
                maxproduct=A[i]*A[j]
                pairs=str(A[i]) + "," + str(A[j])
    print(pairs)
    print(maxproduct)

A=[int(x) for x in input().strip().split()]
maxproduct(A)


            
