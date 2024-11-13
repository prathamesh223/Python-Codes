import sys
sys.setrecursionlimit(2000)

def  quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=len(arr)//2
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x> pivot]
    return quick_sort(left)+middle+quick_sort(right)

arr=[5,3,8,6,2,6,8,9,1]
print(quick_sort(arr))