def permute(A1,A2):
    if len(A1)!=len(A2):
        return False
    A1.sort()
    A2.sort()
    if A1==A2:
        return True
    else:
        return False

A1=[int(x) for x in input().strip().split()]
A2=[int(x) for x in input().strip().split()]
print(permute(A1,A2))
