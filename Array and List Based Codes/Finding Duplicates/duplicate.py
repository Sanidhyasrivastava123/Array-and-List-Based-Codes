def find(A):
    lis=[]
    for i in A:
        if i in lis:
            print(i)
            return False
        else:
            lis.append(i)

    return True

listi=[int(x) for x in input().strip().split()]
print(find(listi))
            
