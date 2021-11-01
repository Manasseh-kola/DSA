"""
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Quick Sort algorithm to sort the array.
"""
def quickSort(array):
    sortHelper(0,len(array)-1,array)
    return array

def sortHelper(start,end,array):
    if start >= end:
      return

    L = start +1
    P = start
    R = end

    while L <= R:
      if array[L] > array[P] and array[R] < array[P]:
        array[L],array[R] = array[R],array[L]
      if array[L] <= array[P]:
        L+=1
      if array[R] >= array[P]:
        R-=1

    array[R],array[P] = array[P],array[R]
    isSmaller = (R-1-start) < (end -R-1)

    if isSmaller:
      sortHelper(start,R-1,array)
      sortHelper(R+1,end,array)
    else:
      sortHelper(R+1,end,array)
      sortHelper(start,R-1,array)
