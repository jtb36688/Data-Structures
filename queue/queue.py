class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_head(item)
  
  def dequeue(self):
    return self.storage.remove_tail()

  def len(self):
    if not self.storage.head:
      return 0
    else:
      current = self.storage.head
      count = 1
      while current.get_next():
        count += 1
        current = current.get_next()
      return count


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next_node):
        self.next_node = new_next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)
        # if not self.head
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self): 
        if not self.head:
            return None

        # What if linked list has a singled element?

        # if self.head == self.tail # this actually wouldn't work if multiples of same values -- I take it back

        # If the head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure teh tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()

        # otherwise we have more than one element in our list
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def remove_tail(self):
      if not self.tail:
          return None

      if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
      
      else:
        value = self.tail.value
        check = self.head
        while not check.get_next() == self.tail:
          check = check.get_next()
        self.tail = check
        self.tail.set_next(None)
        return value



    def contains(self, value):
        # If linked list is empty, return False
        if not self.head:
            return False
        # Is this above part even needed because current is self.head and if this is None it won't run while loop
        else:
            current = self.head
            while current:
                if value == current.get_value():
                    return True
                else:
                    current = current.get_next()
        
            return False
                
    def add_to_head(self, value):
        # init a node with a value of value
        new_node = Node(value, None)

        # If the linked list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node 
    
        # If it has one item
        elif not self.head.get_next():
            new_node.set_next(self.head)
            self.head = new_node
            
        # If it has 2 or more items
        else:
            prev_head = self.head
            self.head = new_node
            self.head.set_next(prev_head)
