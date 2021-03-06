"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    newhead = ListNode(value, None, self.head)
    if self.head:
      self.head.prev = newhead
    else:
      self.tail = newhead
    self.head = newhead
    self.length += 1

  def remove_from_head(self):
    oldhead = self.head
    newhead = self.head.next
    if not self.head.next:
      self.tail = None
    self.head.delete()
    self.head = newhead
    self.length -= 1
    if oldhead.value:
      return oldhead.value
    else:
      return None

  def add_to_tail(self, value):
    newtail = ListNode(value, self.tail, None)
    if self.tail:
      self.tail.next = newtail
    else:
      self.head = newtail
    self.tail = newtail
    self.length += 1

  def remove_from_tail(self):
    oldtail = self.tail
    if not self.head.next:
      self.head = None
    newtail = self.tail.prev
    self.tail.delete()
    self.tail = newtail
    self.length -= 1
    if oldtail.value:
      return oldtail.value
    else:
      return None

  def move_to_front(self, node):
    if node is self.head:
      return
    if node is self.tail:
      self.tail = self.tail.prev
    self.length -= 1
    node.delete()
    if not self.head.next:
      self.tail = self.head
    self.add_to_head(node.value)

  def move_to_end(self, node):
    if node is self.tail:
      return
    if node is self.head:
      self.head = self.head.next
    self.length -= 1
    node.delete()
    if not self.tail.prev:
      self.head = self.tail
    self.add_to_tail(node.value)


  def delete(self, node):
    if node == self.head:
      if self.head.next:
        self.head = self.head.next
      else:
       self.head = None
    if node == self.tail:
      if self.tail.prev:
        self.tail = self.tail.prev
      else:
       self.tail = None
    self.length -= 1
    node.delete()
    
  def get_max(self):
    check = self.head
    maxnode = self.head
    while check.next:
      if check.next.value > check.value:
        maxnode = check.next
      check = check.next
    return maxnode.value

