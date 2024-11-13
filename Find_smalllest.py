def find_smallest(arr):
    smallest=arr[0]
    for num in arr:
        if num <smallest:
            smallest=num
    return smallest
arr=[7,8,1,3,2]
print(find_smallest(arr))