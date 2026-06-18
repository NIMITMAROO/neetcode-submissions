class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}
        arr = []

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hash:
                arr = [hash[complement], i]
            hash[num] = i

        return arr


        