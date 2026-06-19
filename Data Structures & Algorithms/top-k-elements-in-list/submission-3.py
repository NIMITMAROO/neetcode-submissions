class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(list)

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        sorted_item = sorted(count.items(), key = lambda x:x[1], reverse = True)
        
        final_index = []

        for i in range(0,k):

            final_index.append(sorted_item[i][0])
        
        return final_index


        