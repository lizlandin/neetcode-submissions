class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        respuesta = [0] * n

        # El stack guarda índices, NO temperaturas
        stack = []

        # Recorremos los índices de temperatures
        for i in range(n):

            # Mientras el stack no esté vacío y la temperatura
            # actual sea mayor que la temperatura del último
            # índice guardado en el stack
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:

                # Sacamos el índice del stack
                j = stack.pop()

                # Calculamos cuántos días pasaron
                respuesta[j] = i - j

            # Guardamos el índice actual
            stack.append(i)

        return respuesta