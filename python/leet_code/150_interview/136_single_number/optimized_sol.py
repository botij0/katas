from typing import List

# Repaso Lógica XOR:
#
# Devuelve 0 si son iguales y 1 si son distintos.
# La clave está en que los repetidos solo lo están como mucho 2 veces.
#
# Por tanto se puede aplicar la propiedad de XOR:
#
# A ^ B ^ A = B
# B ^ A ^ A = B


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = nums[0]

        for i in range(1, len(nums)):
            curr ^= nums[i]

        return curr


if __name__ == "__main__":
    nums = [2, 2, 5, 3, 3]
    print(Solution().singleNumber(nums))
