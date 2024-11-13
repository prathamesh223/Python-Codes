def count_number_vowels_consonants(s):
    vowels="aeiouAEIOU"
    v_count=sum(1 for i in s if i in vowels)
    c_count=sum(1 for i in s if i.isalpha() and i not in vowels)
    return v_count,c_count
s="abcde"
print(count_number_vowels_consonants(s))