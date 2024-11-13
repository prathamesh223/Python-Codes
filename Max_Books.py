def max_books(books,H,S):
    if S<2:
        return 0
    books.sort()
    t=c=0
    for i in books:
        if t+i <=H:
            t+=i
            c+=1
        else:
            break
    return c
books=list(map(int,input().split()))
H=int(input())
S=int(input())
print(max_books(books,H,S))