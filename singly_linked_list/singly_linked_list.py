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

    def contains(self, value):
        # first let's check if the list is not empty
        if self.head == None:
            return 
        
        # get the first Node of the list
        current = self.head
        # start the loop
        while current:
            # if the Node has the same value with the input
            # return True
            if current.get_value() == value:
                return True
            # update the current node to the next node in list
            # to keep looping through the list
            current = current.get_next()
        # return False if value isn't in the list
        return

    def remove_head(self):
        # if we have an empty LL
        if self.head is None and self.tail is None:
            return
        # if there is a single element in the LL
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head ref
            self.head = None
            # delete the linked list's tail ref
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        # update the current node to the next node in list
        # to keep looping through the list
        self.head = self.head.get_next()
        return val

    def get_max(self):
        if self.head == None:
            return None
        # create a variable for max value
        max_value = self.head.get_value()
        # get the head node for looping
        current = self.head
        # check the list
        while current:
            # check if the current value is greater than max value
            if current.get_value() > max_value:
                # update if current is greater than max
                max_value = current.get_value()
            # update the current node to the next node in list
            # to keep looping through the list
            current = current.get_next()
        return max_value
