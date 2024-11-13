def isPowerofthree(n):
    if n <= 0:
        return False
    while n%3 ==0 :
        n=n//3
    return n==1
n=int(input())
print(isPowerofthree(n))