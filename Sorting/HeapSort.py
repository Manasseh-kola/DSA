"""
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Heap Sort algorithm to sort the
array.

"""
import heapq
def heapSort(array):
    length = len(array)
    heapq.heapify(array)
    return [heapq.heappop(array) for i in range(length)]
