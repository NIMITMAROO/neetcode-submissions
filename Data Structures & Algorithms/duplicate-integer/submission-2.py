class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = defaultdict(list)
        flag = False

        for num in nums:
            seen[num].append(num)
        
        for val in seen.values():
            if len(val) > 1:
                flag = True

        return flag 
        



        
        