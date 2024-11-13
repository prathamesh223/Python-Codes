
num=int(input("Enter the positive number :"))
if num < 2:
    print("Number is not prime")
for i in range(2,int(num**0.5)+1):
    if(num % i)==0:
        print("Number is not prime")
        break
    else:
        print("Number is prime")



