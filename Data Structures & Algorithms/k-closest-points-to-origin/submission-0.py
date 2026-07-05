class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for x,y in points:
            our_tuple = (x**2+y**2,x,y)
            min_heap.append(our_tuple)
        
        return_list = []
        heapq.heapify(min_heap)
        for i in range(k):
            range_origin,x,y = heapq.heappop(min_heap)
            return_list.append([x,y])

        return return_list
