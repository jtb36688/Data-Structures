class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
# append the last value, then bubble up
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    deleted = self.storage.pop(0)
    print("deleted value", deleted)
    if len(self.storage) > 1:
      temp = self.storage[-1]
      self.storage[-1] = self.storage[0]
      self.storage[0] = temp
    self._sift_down()
    return deleted
    # delete, then swap first and last node to maintain structure, then sift down

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
  # checking parent of index
    parentindex = (index-1) // 2
    if self.storage[index] > self.storage[parentindex]:
      temp = self.storage[index]
      self.storage[index] = self.storage[parentindex]
      self.storage[parentindex] = temp
      if not parentindex == 0:
        self._bubble_up(parentindex)

  def _sift_down(self):
    end = len(self.storage) - 1
    print("sift down runs", self.storage)
    for i in self.storage:
      index = i-1
      leftchildindex = 2*index + 1
      rightchildindex = leftchildindex + 1
      if index == 3:
        print("2 running with left index of", leftchildindex)
      if leftchildindex <= end:
        prioritychild = leftchildindex
        if self.storage[index] == 5:
          print("5 is being check against", self.storage[prioritychild])
        if rightchildindex <= end and self.storage[rightchildindex] > self.storage[prioritychild]:
          print("right was greater", self.storage[rightchildindex])
          prioritychild = rightchildindex
        if self.storage[prioritychild] > self.storage[index]:
            print("swap made between", self.storage[prioritychild], self.storage[index])
            temp = self.storage[prioritychild]
            self.storage[prioritychild] = self.storage[index]
            self.storage[index] = temp
            return self._sift_down()
      else:
        if index <= end and self.storage[index] == 5:
          print("check failed for 5 with lci of", leftchildindex)
            


    # if leftchildindex <= end:
    #   prioritychild = leftchildindex
    #   while index <= end:
    #     print(self.storage[prioritychild])
    #     if rightchildindex <= end and self.storage[rightchildindex] > self.storage[prioritychild]:
    #       prioritychild = rightchildindex
    #       print("right child used", self.storage[prioritychild])
    #     if self.storage[prioritychild] > self.storage[index]:
    #       temp = self.storage[prioritychild]
    #       self.storage[prioritychild] = self.storage[index]
    #       self.storage[index] = temp
    #       index = prioritychild
    #       leftchildindex = 2*index + 1
    #       rightchildindex = leftchildindex + 1
    #     else:
    #       break


        
       

    # check both left and right are defined, and compare to parent. 
    # assure parent is greater than children
    # if both are larger, swap with whichever child is larger

