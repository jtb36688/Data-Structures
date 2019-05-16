class Heap:
  def __init__(self, comparator=lambda x, y: x > y):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    if not len(self.storage):
      return self.storage.append(value)
    inserted = False
    currentitem = self.storage.index[0]
    while not inserted:
      currentindex = self.storage.index(currentitem)
      leftchild = self.storage[2 * currentindex + 1]
      leftindex = 2 * currentindex + 1
      rightchild = self.storage[2 * currentindex + 2]
      rightindex = 2 * currentindex + 2
      if not self.comparator(value, currentitem):
        if leftchild:
          if not rightchild:
            if value >= leftchild:
              inserted = True
              self.storage.insert(leftindex, value)
          else:
        else:
          inserted = True
          self.storage.insert(rightindex, value)
        


          
        

  def delete(self):
    pass

  def get_priority(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
