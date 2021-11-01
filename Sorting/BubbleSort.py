def bubbleSort(array):
    notSorted = True
    count = 0

    while notSorted:
      notSorted = False
      for i in range(len(array)-count-1):
        if array[i] > array[i+1]:
          notSorted = True
          array[i],array[i+1] = array[i+1],array[i]
    return array
