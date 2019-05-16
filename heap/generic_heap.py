class Heap:
  def __init__(self, comparator=None):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    if not len(self.storage):
      self.storage.append(value)
    if not self.comparator:
      for item in self.storage:
        if value >= item:
          return self.storage.insert(self.storage.index(item), value)
        else:
          if self.storage.index(item) == len(self.storage)-1:
            self.storage.append(value)
        

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
