def selection_sort(Arr):
    for i in range(len(Arr)):
        min_index=i
        for j in range(i+1,len(Arr)):
            if(Arr[j]< Arr[i]):
                min_index=j
        Arr[i],Arr[min_index]=Arr[min_index],Arr[i]
    return Arr
Arr=[5,3,8,6,2]
print(selection_sort(Arr))
        