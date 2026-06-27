class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []

        for i in range(len(numbers)):
            complement = target - numbers[i]
            for j in range(len(numbers)):
                if complement == numbers[j] and i != j:
                    out.append(i+1) 
                    out.append(j+1) 
                    return out
                else:
                    continue
        