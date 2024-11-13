import sys
a=int(input("Enter the number of students place in CSE Department :-"))
b=int(input("Enter the number of students place in ECE Department :-"))
c=int(input("Enter the number of students place in MECH Department :-"))

if a<0 and b<0 and c<0:
    print("Invalid Input")
    sys.exit()
elif(a==b and b==c):
    print("All the departments have equal number of students")
    sys.exit()
elif(a>b and a>c):
    print("CSE Department has highest placement")
elif(b>a and b>c):
    print("ECE Department has highest placement")
elif(a==b):
    print("CSE and ECE Department has highest placement")
elif(b==c):
    print("ECE and MECH Department has highest placement")
elif(a==c):
    print("CSE and MECH Department has highest placement")
else:
    print("MECH Department has highest placement")
