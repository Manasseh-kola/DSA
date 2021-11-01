"""
Write a function that takes in an array of nonnegative integers and returns a sorted version
of that array. Use the Radix Sort algorithm to
sort the array.


Sample Input
array = [8762, 654, 3008, 345, 87, 65,234,12,2]

Sample Output
array = [2, 12, 65, 87, 234, 345, 654, 3008, 8762]
"""

def radixSort(array):
      if len(array) == 0:
      return array

    maxNumber = max(array)
    digit = 0
    while maxNumber // 10 ** digit >0 :
      array = countingSort(array,digit)
      digit +=1

    return array

def countingSort(array,digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10

    digitColumn = 10 ** digit
    for num in array:
      countIndex = (num//digitColumn) % 10
      countArray[countIndex] +=1

    for i in range(1,10):
      countArray[i] += countArray[i-1]

    for i in range(len(array)-1,-1,-1):
      countIndex = (array[i]//digitColumn)%10
      countArray[countIndex] -=1
      sortedIndex = countArray[countIndex]
      sortedArray[sortedIndex] = array[i]

    return sortedArray
