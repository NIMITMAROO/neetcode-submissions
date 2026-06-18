class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(list)

        freq = []
        final_index = []
        sort_dict = []
        

        for i,num in enumerate(nums):

            count[num] = count.get(num,0) + 1
        
        sort_dict = list(sorted(count.items(), key = lambda x:x[1], reverse = True))

        i = 0 
        while i != k:
            final_index.append(sort_dict[i][0])
            i += 1
        
        return final_index
            





        







        