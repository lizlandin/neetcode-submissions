class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {}
        word_2 = {}

        if len(s) != len(t):
            return False 
        else: 

            for char in s:
                if char not in word_1:
                    word_1[char] = 1
                else:
                    word_1[char] += 1

            
            for char in t:
                if char not in word_2:
                    word_2[char] = 1
                else:
                    word_2[char] +=1
            
            if word_1 == word_2:
                return True
    
        return False
            


        
 

