class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        zero_count = 0
        tot = 1
        tot_1z = 1 # One zero

        for i,num in enumerate(nums):
            if num == 0:
                zero_count += 1
                tot = tot * num
            
            else:
                tot = tot * num
                tot_1z = tot_1z * num

        for i,num in enumerate(nums):
            if zero_count == 1 and num == 0:
                out.append(int(tot_1z))
            
            elif zero_count > 1:
                out.append(0)
            
            else:
                out.append(int(tot/num))
        
        return out
        