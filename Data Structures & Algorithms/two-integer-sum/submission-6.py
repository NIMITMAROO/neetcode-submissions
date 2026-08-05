class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)


        for i,n in enumerate(nums):
            seen[n] = i
        
        for j,num in enumerate(nums):
            a = target - num
            if a in seen and seen[a] != j:
                return [j,seen[a]]


        