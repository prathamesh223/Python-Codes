def second_lar(arr):
    if len(arr) < 2:
        return None
    first,second=float('-inf'),float('-inf')
    for i in arr:
        if i>first:
            second=first
            first=i
        elif first > i > second :
            second=i
    return second
arr=[1,5,6,9,4]
print(second_lar(arr))