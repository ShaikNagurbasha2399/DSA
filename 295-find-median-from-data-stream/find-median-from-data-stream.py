class MedianFinder:
    #Here is the actual expected optimised code
    def __init__(self):
        #store first half of the sorted elements in a MaxHeap
        self.first = []
        #store second half of the sorted elements in a MinHeap
        self.second = []
        #But in python, default heap i.e. heapq is MinHeap only. there is no max heap.
        #Hence store the -ve num is first list to get it work like maxHeap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first, -1*num) #this is to make the heapq work like MaxHeap
        #pop and push for heap takes O(logn) time
        #1. make sure 1st heap has all elements < 2nd heap
        if (self.first and self.second and
            -1*(self.first[0]) > self.second[0]):
            n = -1*heapq.heappop(self.first)
            heapq.heappush(self.second, n)

        #2a. size diff of 1st & 2nd should not be >1
        if len(self.first)>len(self.second)+1:
            n = -1*heapq.heappop(self.first)
            heapq.heappush(self.second, n)
        #2b
        if len(self.second)>len(self.first)+1:
            n = heapq.heappop(self.second)
            heapq.heappush(self.first, -1*n)

    def findMedian(self) -> float:
        #Fetching Min from MinHeap and Max from MaxHeap is gonna take only O(1) time
        if len(self.first) > len(self.second): 
            #means odd num of elements
            return -1*self.first[0]
        if len(self.second) > len(self.first): 
            #means odd num of elements
            return self.second[0]
        else:
            #both have same num of elements -- totally even elements
            return (-1*self.first[0]+self.second[0])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()