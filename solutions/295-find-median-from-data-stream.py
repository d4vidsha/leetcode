class MedianFinder:

    def __init__(self):
        # upper list
        self.minHeap = []
        # lower list
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # O(logn)
        # add to correct heap
        if self.minHeap and self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # ensure balanced
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) - len(self.minHeap) < -1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
    def findMedian(self) -> float:
        # O(1)
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            return 0
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
