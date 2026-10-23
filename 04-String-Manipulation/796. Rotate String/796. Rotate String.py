1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3
4        letras = list(s)
5        meta = list(goal)
6
7        for i in range(len(letras)):
8            if letras != meta:
9                letras.append(letras[0])
10                letras.pop(0)
11
12            elif letras == meta:
13                return True 
14
15        return False 
16
17
18
19
20
21             
22
23
24
25        