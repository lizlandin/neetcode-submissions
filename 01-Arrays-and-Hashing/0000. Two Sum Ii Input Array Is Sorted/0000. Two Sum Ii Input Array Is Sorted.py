class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        respuesta = []

        left = 0
        right = len(numbers) - 1

        while left < right:
            suma = numbers[left] + numbers[right]

            if suma > target:
                right -= 1
            elif suma < target:
                left += 1
            elif suma == target:
                respuesta.append(left + 1)
                respuesta.append(right + 1)
                return respuesta
