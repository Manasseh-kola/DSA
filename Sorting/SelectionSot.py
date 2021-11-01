def selectionSort(array):
    currentIdx = 0

    while currentIdx < len(array):
      smallest = currentIdx

      for i in range(currentIdx,len(array)):
        if array[i] < array[smallest]:
          smallest = i

      array[smallest],array[currentIdx] = array[currentIdx],array[smallest]
      currentIdx+=1
    return array
