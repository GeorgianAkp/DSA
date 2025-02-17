'''
1. Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
'''
#1 Approach1 : Using an array of boolean values to keep track of the characters that have been seen.Second time we see a character we return False.
# Time complexity : O(n)
# Space complexity : O(1) , as the size of the array is fixed.

def isUnique(str):
    if len(str) > 128 : 
        return False 
    char_set = [False for _ in range(128)]
    for ch in str : 
        if char_set[ord(ch)]:
            return False 
        char_set[ord(ch)] = True 
    return True

print(isUnique('abcA 83'))