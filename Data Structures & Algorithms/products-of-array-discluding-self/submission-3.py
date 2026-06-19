class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        out = [1] * n

        # Left products
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]

        # Right products
        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]

        return out