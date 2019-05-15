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
    self.tail = newtail
    if not self.head:
      self.head = newtail
    self.length += 1

  def remove_from_tail(self):
    oldtail = self.tail
    if not self.head.next:
      self.head = None
    newtail = self.tail.prev
    print("newtail", newtail)
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
    self.length -= 1
    # line 94 is required because the node delete method doesn't decrease length
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    found = False
    while not found:
      print("movetoend")
      check = self.head
      if check == node:
        found = True
      else:
        if check == self.tail:
          return
        check = check.next
    if check == self.tail:
      return
    check.delete()
    self.tail.next = check
    check.prev = self.tail
    check = self.tail


  def delete(self, node):
    found = False
    while not found:
      print("deleting")
      check = self.head
      if check == node:
        found = True
      else:
        if check == self.tail:
          return
        check = check.next
    check.delete()
    
  def get_max(self):
    check = self.head
    maxnode = self.head
    while check.next:
      if check.next.value > check.value:
        maxnode = check.next
      check = check.next
    return maxnode.value

