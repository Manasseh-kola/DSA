"""
Write a function that takes in an array of distinct integers as well as an integer k and that returns the kth smallest integer in that array.
The function should do this in linear time, on average.

Sample Input
array = [8, 5, 2, 9, 7, 6, 3]
k = 3
Sample Output
5

"""

def quickselect(array, k):
    skip = {}
    ksmall = None
    for _ in range(k):
      smallest = None
      for i,num in enumerate(array):
        if i in skip:
          continue
        if smallest is None:
          smallest = i
        elif num < array[smallest]:
          smallest = i
      skip[smallest] = True
      ksmall = array[smallest]

    return ksmall
