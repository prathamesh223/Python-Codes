def is_prime(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5) +1):
        if (n % i)==0 :
            return False
    return True
def prime_num_interval(a,b):
    if(a>=0 and b>=0 and a<=b):
        for num in range(a,b+1):
            if is_prime(num):
                print(num,end=' ')
    
    else:
        print("Invalid Input")


a=int(input())
b=int(input())
prime_num_interval(a,b)        