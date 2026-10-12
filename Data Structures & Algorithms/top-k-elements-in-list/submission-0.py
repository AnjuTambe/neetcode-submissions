class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        heap = []

        result = []

        for num in nums : 

            freq[num] = freq.get(num , 0) + 1

        for num , count in freq.items() : 
                heapq.heappush(heap , (count , num))

                if len(heap) > k : 
                    heapq.heappop(heap) 

        for count , num in heap : 
                result.append(num)

        return result        




              


        