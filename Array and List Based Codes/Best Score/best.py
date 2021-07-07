def bestscore(A):
    A.sort(reverse=True)
    first=A[0]
    second=None
    for i in A:
        if i != first:
            second=i
            return first,second

A=[1,5,7,3,9,2]
print(bestscore(A))
