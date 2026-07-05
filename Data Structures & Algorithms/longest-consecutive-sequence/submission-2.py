class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set()
        curr = 0
        l = 0
        longest = 0
        hash.update(nums)

        for i,num in enumerate(nums):

            if num - 1 not in hash:
                curr = num
                l = 1
                while curr + 1 in hash:
                    curr += 1
                    l += 1

                if longest < l:
                    longest = l
        
        return longest

         
