class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        ht = heights
        start = 0
        end = len(heights) - 1

        while start < end:
            h = min(ht[start], ht[end])
            b = end - start

            if h * b > area:
                area = h * b
            
            if ht[start] < ht[end]:
                start += 1
            
            elif ht[start] >= ht[end]:
                end -= 1

        return area
            



        