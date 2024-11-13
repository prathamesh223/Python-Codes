def house_visit(House,N):
    if N== 0:
        return 0
    if N==1:
        return 1
    s=1
    c=0
    while s <= N:
        c+=1
        s+=House[s-1]
    return c
N=int(input())
House=list(map(int,input().split()))

print(house_visit(House,N))