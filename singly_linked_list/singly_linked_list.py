class Node:
    def __init__(self, value=None, next_node=None):

        # init of every Node should have a value
        self.value = value

        # a pointer that point to the next node
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        # init of empty LL should have both head 
        # and tail set to None
        self.head = None
        self.tail = None

    # return all values in the list a -> b -> c -> None
    def __str__(self):
        output = ''
        current_node = self.head # create a tracker variable
        while current_node is not None: # loop until its NONE
            output += f"{current_node.value} -> "

            # update the tracker node to the next node
            current_node = current_node.next_node 
        return output

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node


    def add_to_tail(self, value):
        # make a new Node to add
        new_node = Node(value)
        # check if the list empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if not empty, set tail's pointer pointing 
        # to the new Node
        # Then set tail to be the new Node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def contains(self, value):
        # first let's check if the list is not empty
        if self.head == None:
            return False
        
        # Loop through each node, until we see the value,
        # or we can't go further
        current = self.head

        while current:
            # check if this is the node we are looking for
            if current.value == value:
                return True
            
            # otherwise, go to the next node
            current = current.next_node
        # return False if value isn't in the list
        return False

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            # we need to get the head_value so we could return it
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value

        # otherwise
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    
    # remove the head and return its value
    def remove_tail(self):
        # if list is empty, do nothing
        if not self.tail:
            return None
        
        # if list has one element, set both head and tail to None
        if self.head == self.tail:
            # we need to get the tail_value so we could return it
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value
        
        # otherwise
        current = self.head
        while current:
            if current.next_node == self.tail:
                tail_value = current.next_node.value
                self.tail = current
                self.tail.next_node = None
                return tail_value
            current = current.next_node

    def get_max(self):
        # if list is empty, do nothing
        if self.head == None:
            return None

        # create a variable for max value
        max_value = self.head.value

        # get the head node for looping
        current = self.head
        # check the list
        while current:
            # check if the current value is greater than max value
            if current.value > max_value:
                # update if current is greater than max
                max_value = current.value
            # set the current node to the next Node
            # to keep looping through the list
            current = current.next_node
        return max_value


ll = LinkedList()
ll.add_to_head(0)
ll.add_to_tail(1)

ll.remove_tail()

print(ll)