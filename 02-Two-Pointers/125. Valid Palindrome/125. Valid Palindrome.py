1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = s.lower()
4
5        left = 0
6        right = len(s) - 1
7
8        while left <= right:
9
10            if not s[left].isalnum():
11                left += 1
12
13            elif not s[right].isalnum():
14                right -= 1
15            
16            elif s[left] != s[right]:
17                return False
18            else:
19                left += 1
20                right -= 1
21
22        return True 
23        
24
25