def string_character_removal(S:str)->int:
    removal_count=0
    for i in range(1,len(S)-1):
        if (S[i]) == (S[i+1]):
            removal_count+=1
    return removal_count
s="XYXXYXXY"
print(string_character_removal(s))