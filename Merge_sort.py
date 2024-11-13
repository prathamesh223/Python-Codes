# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     l_half=merge_sort(arr[:mid])
#     r_half=merge_sort(arr[mid:])
#     return merge(l_half,r_half)
# def merge(left,right):
    
#     new=[]
#     i,j=0,0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             new.append(left[i])
#             i+=1
#         else:
#             new.append(right[j])
#             j+=1
#     new.extend(left[i:])
#     new.extend(right[j:])
#     return new        
# arr=[12, 11, 13, 5, 6, 7]
# print("Given array is",arr)
# print(merge_sort(arr))
# def merge_sort(arr):

#     # Base case: If the array is of length 1 or less, return it as it is already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Find the middle of the array
#     mid = len(arr) // 2
    
#     # Recursively split and sort the left and right halves
#     l_half = merge_sort(arr[:mid])
#     r_half = merge_sort(arr[mid:])
    
#     # Merge the sorted halves
#     return merge(l_half, r_half)

# def merge(left, right):
#     i, j = 0, 0
#     new = []
    
#     # Merge process to combine left and right halves in sorted order
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             new.append(left[i])
#             i += 1
#         else:
#             new.append(right[j])
#             j += 1
    
#     # Append any remaining elements
#     new.extend(left[i:])
#     new.extend(right[j:])
    
#     return new  # Ensure merge function returns the merged list

# # Example usage:
# arr = [12, 11, 13, 5, 6, 7]
# sorted_arr = merge_sort(arr)  # Store the result of merge_sort
# print("Sorted array is:", sorted_arr)
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_half=merge_sort(arr[:mid])
    r_half=merge_sort(arr[mid:])
    return merge(l_half,r_half)
def merge(left,right):
    i,j=0,0
    new=[]
    while i<len(left) and j<len(right):
        if(left[i] <right[j]):
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
arr=[12,4,54,7,1,54,9,10]
m=merge_sort(arr)
print(m)


        