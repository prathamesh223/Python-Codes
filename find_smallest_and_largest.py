def small_large(arr):
    min_num=max_num=arr[0]
    for i in arr:
        if i<min_num:
            min_num=i
        elif i>max_num:
            max_num=i
    return min_num,max_num
arr=[5,3,8,6,2,9,1]
print(small_large(arr))