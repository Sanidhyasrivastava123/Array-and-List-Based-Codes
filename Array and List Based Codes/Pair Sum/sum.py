def find(A,target):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i]==A[j]:
                continue
            elif A[i]+A[j]==target:
                print(i,j)


mylist=[int(x) for x in input().strip().split()] 
c=6
find(mylist,c)
