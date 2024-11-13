def count_pen_switches(N,num):
    if N==0:
        return 0
    switches =0
    for i in range(1,N-1):
        if (num[i]%2) != (num[i+1]%2):
            switches +=1
    return switches
N=4
num=[1,3,4,5]
print(count_pen_switches(N,num))