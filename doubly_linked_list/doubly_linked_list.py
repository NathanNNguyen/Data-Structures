"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleteing this ListNode."""
    # def delete(self):
    #     if self.prev:
    #         self.prev.next = self.next
    #     if self.next:
    #         self.next.prev = self.prev
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        output = ''
        current_node = self.head # create a tracker variable

        while current_node: # loop until its NONE
            output += f"{current_node.value} -> "

            # update the tracker node to the next node
            current_node = current_node.next
        return output

    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # make a node
        new_node = ListNode(value)
        self.length += 1
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        # otherwise
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # pass
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # check for list is empty
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value

        # check if list is empty
        # if not self.head:
        #     return None
        
        # # if there is only 1 item in the list
        # if self.head.next is None:
        #     head_value = self.head.value
        #     self.head == None
        #     self.tail == None
        #     # self.length -= 1
        #     return head_value

        # # otherwise
        # head_value = self.head.value
        # self.head = self.head.next
        # self.head.prev = None
        # # self.length -= 1
        # return head_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.tail is None and self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if list is empty -> do nothing
        if self.head is None and self.tail is None:
            return None

        self.length -= 1
        # the list has one node
        # extra condition to check if someone given
        # the node that's not even in the list
        if self.head == self.tail and node is self.head:
            self.head = None
            self.tail = None

        # the node is the HEAD node (handle pointer correctly)
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
            # node.delete()

        # the node is the TAIL node (handle pointer correctly)
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            # node.delete()

        # the node is just some node in the list
        else:
            # node.delete()

            # check if the node has at least one node
            # for it previous and next
            if node.prev and node.next:
                prev_node = node.prev
                next_node = node.next

                prev_node.next = next_node
                next_node.prev = prev_node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass


dl = DoublyLinkedList()
dl.add_to_head(2)
dl.add_to_head(3)
dl.add_to_head(5)
dl.remove_from_head()
dl.remove_from_head()
print(dl)