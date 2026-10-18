class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for simbolo in s:
            if simbolo in "([{":
                stack.append(simbolo)
            
            else:
                if len(stack) == 0:
                    return False 
                ultimo = stack.pop()

                if simbolo == ")" and ultimo != "(":
                    return False 
                if simbolo == "]" and ultimo != "[":
                    return False 
                if simbolo == "}" and ultimo != "{":
                    return False 
        
        if len(stack) == 0:
            return True  
        else:
            return False 












