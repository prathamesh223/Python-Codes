#  Write a program to check whether the given string is pangram or not.
# Solution :- In this program we will check whether the given string is pangram or not.

# Pangram :- If a string contains every letter of the English alphabet i.e all 26 alphabets then the string is known as Pangram.

import string 
def check_pangram(str1):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str1.lower():
            return False
    return True
string1="The quick brown fo jumps over the lazy dog"
if(check_pangram(string1)==True):
    print("The string is a Pangram")
else:
    print("The string is not a Pangram")