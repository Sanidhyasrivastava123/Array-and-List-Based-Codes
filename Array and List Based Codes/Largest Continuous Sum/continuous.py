def continsum(A):
    if len(A)==0:
        return 0
    max_sum=curr_sum=A[0]
    for i in A[1:]:
        curr_sum=max(curr_sum+i,i)
        max_sum=max(curr_sum,max_sum)

    return max_sum

A=[int(x) for x in input().strip().split()]
print(continsum(A))

        
