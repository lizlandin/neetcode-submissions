class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if (len(stack) == 0) or (char not in "+-/*"):
                stack.append(int(char))

            elif char == "+":
                suma = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(suma)
            elif char == "-":
                resta = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(resta)
            elif char == "/":
                division = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(division)
            else:
                multiplicacion = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(multiplicacion)
        
        return stack.pop()


