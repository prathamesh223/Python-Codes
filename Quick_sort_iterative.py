def quick_sort(arr,low,high):
    if low < high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    return arr
def partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j
arr=[12, 11, 13, 5, 6, 7]
print("Given array is",arr)
print(quick_sort(arr,0,len(arr)-1))


# def quick_sort(arr,low,high):
#     if low < high:
#         pivot=partition(arr,low,high)
#         quick_sort(arr,low,pivot-1)
#         quick_sort(arr,pivot+1,high)
#     return arr
# def partition(arr,low,high):
#     p=arr[low]
#     i=low+1
#     j=high
#     while True:
#         while i<=j and arr[i]<=p:
#             i+=1
#         while i<=j and arr[j]>=p:
#             j-=1
#         if i<=j:
#             arr[i],arr[j]=arr[j],arr[i]
#         else:
#             break
#     arr[low],arr[j]=arr[j],arr[low]
#     return j
# arr=[12,5,7,54,74,5]
# m=quick_sort(arr,0,len(arr)-1)
# print(m)