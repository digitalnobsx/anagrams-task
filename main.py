# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    str1 = input("Enter a word: ")
    str2 = input("Enter another word: ")
    if sorted(str1) == sorted(str2):
        print("True")
    else:
        print("False")


find_anagram('str1', 'str2')
