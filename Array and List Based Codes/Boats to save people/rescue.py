def rescue(A,limit):
    A.sort()
    n=len(A)
    left=0
    right=len(A)-1
    boats_number=0
    while(left<=right):
          if(left==right):
                boats_number+=1
                break
        
          if(A[left]+A[right]<=limit):
                left+=1
                
                
          right-=1
          boats_number+=1

    return boats_number


A=[int(x) for x in input().strip().split()]
limit=int(input())
print(rescue(A,limit))

          
