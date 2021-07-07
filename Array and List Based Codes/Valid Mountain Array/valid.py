def validMountainArray(A):
        if(len(A)<3):
            return False
        
        i = 1
        while(i<len(A) and A[i]>A[i-1]):
            i+=1
        
        if(i==1 or i==len(A)):
            return False
        
        while(i<len(A) and A[i]<A[i-1]):
            i+=1
        
        return i==len(A)
A=[int(x) for x in input().strip().split()]
print(validMountainArray(A))
