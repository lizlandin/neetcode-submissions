1class Solution:
2    def restoreString(self, s: str, indices: list[int]) -> str:
3
4       
5        n = len(indices)
6        shuffle = [0] * n 
7
8        for i in range(len(s)):
9            letra = s[i]
10            posicion = indices[i]
11
12            shuffle[posicion] = letra
13        
14        respuesta = .join(shuffle)
15
16        return respuesta 
17
18
19
20
21
22
23
24
25
26
27
28
29        