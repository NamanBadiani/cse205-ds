import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        self.k = k
        
        for num in nums[k:]:
            self.add(num)

    def add(self, val: int) -> int:
        
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
       
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]