class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
# append the last value, then bubble up
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    deleted = self.storage.pop(0)
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
    for i in range(len(self.storage)):
      index = i
      leftchildindex = 2*index + 1
      rightchildindex = leftchildindex + 1
      if leftchildindex <= end:
        prioritychild = leftchildindex
        if rightchildindex <= end and self.storage[rightchildindex] > self.storage[prioritychild]:
          prioritychild = rightchildindex
        if self.storage[prioritychild] > self.storage[index]:
            temp = self.storage[prioritychild]
            self.storage[prioritychild] = self.storage[index]
            self.storage[index] = temp
            return self._sift_down()
      
    # check both left and right are defined, and compare to parent. 
    # assure parent is greater than children
    # if both are larger, swap with whichever child is larger

