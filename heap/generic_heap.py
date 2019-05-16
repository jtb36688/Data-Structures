class Heap:
  def __init__(self, comparator=lambda x, y: x > y):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    if not len(self.storage):
      self.storage.append(value)
    found = False
    while not found:
      currentitem = self.storage.index[0]
      if not self.comparator(value, currentitem):
        if self.storage[2 * self.storage.index(currentitem) + 1]:
          if not self.storage[2 * self.storage.index(currentitem) + 2]:
      else:

          
        

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
