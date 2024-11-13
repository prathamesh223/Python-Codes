# def reverse_string(input_string):
#     reversed_str = ""
#     for char in input_string:
#         reversed_str = char + reversed_str
#     return reversed_str

# # Example usage:
# result = reverse_string("Hello World")
# print(result)  # Output: "dlroW olleH


#Reverse a string using a loop
def reverese_string(input_string):
    reverse_str=""
    for i in input_string:
        reverse_str=i+reverse_str
        print(reverse_str)
    return reverse_str
result=reverese_string("Hello World")
print(result)




def pattern_1(N):
    for i in range(N):
        for j in range(N):
            print("*", end=" ")
        print()
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
def pattern_1(N):
    for i in range(N):
        for j in range(N):
            print("*", end=" ")
        print()



N = 5
pattern_1(N)
#Increase the number of stars in each row
def patern1(N):
    for i in range(N):
        for j in range(i+1):
            print("*", end=" ")
        print()
# *
# * *
# * * *
# * * * *
# * * * * *
def pattern1(N):
    for i in range(N):
        for j in range(i+1):
            print(i+1,end=" ")
        print()
N = 5
patern1(N)
def pattern1(N):
    for i in range(N):
        for j in range(i+1):
            print(j+1, end=" ")
        print()
N = 5
pattern1(N)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


def pattern1(N):
    for i in range(N):
        for j in range(i+1):
            print(i+1, end=" ")
        print()
N = 5
pattern1(N)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

#Decrease the number of stars in each row

def patern1(N):
    for i in range(N):
        for j in range(N-i):
            print("*", end=" ")
        print()

# * * * * *
# * * * *
# * * *
# * *
# *
N = 5
patern1(N)


def patern_downword(N):
    for i in range(N):
        for j in range(N-i):
            print(j+1, end=" ")
        print()
N = 5
patern_downword(N)
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def patern_downword(N):
    for i in range(N):
        for j in range(N-i):
            print(i+1, end=" ")
        print()
N = 5
patern_downword(N)
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
