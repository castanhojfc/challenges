"""
Problem:
Find the median of a data stream of integers.

Solution:
Maintain two heaps.
A max heap to hold the lower numbers sorted.
A min heap to hold the higher numbers sorted.
The heap will provide us the middle values in the sorted array instantly if we
keep balancing it.
If their size is different just pick the root of the max heap.
This is because the size of the array is odd and and the median in a sorted
array is always the middle value.
If their size is the same, pick both roots, add them and divide by two.
How do we balance:
If there is no element in the max heap we add this number to it.
We also add it if it us lower or uqual to the root of the min heap.
We move numbers from the min to the max heaps and vice versa when their size
is bigger, this ensures that both of them have the same size.
Actually this is not quite true the max heap always has one extra value.
This extra value is considered when balancing.

Runtimes:
Time:
findMedian(): O(1)
addNum(): O(log(n))
Space:
findMedian() and addNum(): O(n)


https://leetcode.com/problems/find-median-from-data-stream/
"""

from heapq import heapify, heappop, heappush


class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return 0.5 * (self.minHeap[0] - self.maxHeap[0])
        if len(self.maxHeap) == len(self.minHeap) + 1:
            return -self.maxHeap[0]


if __name__ == "__main__":
    medianFinder = MedianFinder()

    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())

    medianFinder = MedianFinder()

    medianFinder.addNum(-1)
    print(medianFinder.findMedian())
    medianFinder.addNum(-2)
    print(medianFinder.findMedian())
    medianFinder.addNum(-3)
    print(medianFinder.findMedian())
    medianFinder.addNum(-4)
    print(medianFinder.findMedian())
    medianFinder.addNum(-5)
    print(medianFinder.findMedian())

    medianFinder = MedianFinder()

    medianFinder.addNum(6)
    print(medianFinder.findMedian())
    medianFinder.addNum(10)
    print(medianFinder.findMedian())
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(6)
    print(medianFinder.findMedian())
    medianFinder.addNum(5)
    print(medianFinder.findMedian())
    medianFinder.addNum(0)
    print(medianFinder.findMedian())
    medianFinder.addNum(6)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
    medianFinder.addNum(1)
    print(medianFinder.findMedian())
    medianFinder.addNum(0)
    print(medianFinder.findMedian())
    medianFinder.addNum(0)
    print(medianFinder.findMedian())
