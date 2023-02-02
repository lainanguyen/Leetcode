"""
Given 2 strings, s ant t
return true if s is a subsequence of t
otherwise return false

subsequence = (of a string) is a new string formed from the original string by deleting some (or none) of the
characters without disturbing the relative positions of the remaining characters

example: "ace" is a subsequence of "abcde" but "aec" is not
case 1:
    input: s = "abc", t = "ahbgdc"
    output: true
case 2:
    input: s = "axc", t = "ahbgdc"
    return: false
"""

"""
[a, b, c]
s 'abc'
t a h b g d c

[a, b]
s abc
t a c b 
if i in s :
    if j in i
    
s abc
t ahgbc

"""


class Solution:
    def isSubsequence(self, s: str, t:str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        else:
            return False





