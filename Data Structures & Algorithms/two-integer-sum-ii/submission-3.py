class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[end] == target - numbers[start]:
                out.append(start + 1)
                out.append(end + 1)
                break

            elif numbers[end] > target - numbers[start]:
                end -= 1

            elif numbers[start] < target - numbers[end]:
                start += 1

            
        return out





