def remove_duplicate(arr):
    unique_element=[]
    seen={}
    for i in arr:
        if i not in seen:
            unique_element.append(i)
            seen[i]=True
    return unique_element