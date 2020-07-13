class Node:
    def __init__(self, value):
        # init of every Node should have a value
        self.value = value
        # a pointer that point to the next node
        # if there's only 1 node, pointer point to None
        self.next = None

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        # for addding a new node, this would help the 
        # pointer pointing to the new Node input
        self.next = new_next

class LinkedList:
    def __init__(self):
        # init of empty LL should have both head 
        # and tail set to None
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # make a new Node
        new_node = Node(value)
        # check for head and tail status
        # if LL is empty, set both to the new Node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if not empty, set tail's pointer pointing 
        # to the new Node
        # Then set tail to be the new Node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    # def contains(self, value):
    #     head_val = self.head.get_value()
    #     tail_val = self.tail.get_value()
    #     if self.tail:
    #         return tail_val
    #     else:
    #         return 
        