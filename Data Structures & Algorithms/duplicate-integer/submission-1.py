class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = []
        flag = False

        for i in nums:

            
            if i not in seen:
                seen.append(i)
            else:
                flag = True
        return flag


        
        