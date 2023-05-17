import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        print(s)
        if len(s)%2 == 0:
            return s[:len(s)//2] == (s[(len(s)//2):][::-1])
        else: 
            return s[:len(s)//2] == (s[(len(s)//2)+1:][::-1])