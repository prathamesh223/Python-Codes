def  first_not_repeating_cahracter(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in s:
        if freq[i]==1:
            return i
        


s="abacabad"
print(first_not_repeating_cahracter(s))
# from collections import Counter

# def first_non_repeating(s):
#     count = Counter(s)
#     for ch in s:
#         if count[ch] == 1:
#             return ch
#     return None

# # Example usage:
# print(first_non_repeating("swiss"))  # Output: "w"
