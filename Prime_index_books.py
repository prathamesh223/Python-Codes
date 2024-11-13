def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+ 1):
        if n%i==0:
            return False
    return True
def prime_index_books(S,K,Books):
    total=0
    for i in range(1,S+1):
        if is_prime(i):
            total+=min(K,Books[i-1])
    return total
S=int(input("Enter the size of an array ---> "))
K=int(input("Enter the number of books maximum select from 1 shelve ----> "))
Books=list(map(int,input().split()))
print(prime_index_books(S,K,Books))