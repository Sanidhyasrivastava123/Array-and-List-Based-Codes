# If had to find the missing number in an array upto a given number
def miss(A,n):
    sum1=n*(n+1)//2
    sum2=sum(A)
    diff=sum1-sum2
    return(diff)

n=int(input())
A=[int(x) for x in input().strip().split()]
print(miss(A,n))
