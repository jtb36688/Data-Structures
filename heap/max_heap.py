class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
# append the last value, then bubble up
    self.storage.append(value)
    self.bubble_up(len(self.storage)-1)

  def delete(self):
    pass
    # delete, then swap first and last node to maintain structure, then sift down

  def get_max(self):
    pass

  def get_size(self):
    pass

  def bubble_up(self, index):
  # checking parent of index
    parentindex = (index-1) // 2
    print(self.storage[index], self.storage[parentindex])
    if self.storage[index] > self.storage[parentindex]:
      print("bubbling up", self.storage[index])
      temp = self.storage[index]
      self.storage[index] = self.storage[parentindex]
      self.storage[parentindex] = temp
      print(self.storage)
      if not parentindex == 0:
        self.bubble_up(parentindex)

    




  def sift_down(self, index):
    pass
    # check both left and right are defined, and compare to parent. 
    # assure parent is greater than children
    # if both are larger, swap with whichever child is larger

