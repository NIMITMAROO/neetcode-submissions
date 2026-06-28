class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        num = numbers
        start = 0
        end = len(numbers) - 1

        while start < end:

            if num[end] + num[start] == target:
                out.append(start + 1)
                out.append(end + 1)
                break
            
            if num[end] >  target - num[start]:
                end -= 1
            
            if num[start] < target - num[end]:
                start += 1
            
        return out
        