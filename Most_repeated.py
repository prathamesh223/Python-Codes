def most(arr):
    freq={}
    max_count=0
    most_repeated=None
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
        if freq[num]>max_count:
            max_count=freq[num]
            most_repeated=num
    return most_repeated
arr = [1, 2, 3, 2, 4, 2, 5, 3, 3]
result = most      (arr)
print("Most repeated element:", result)