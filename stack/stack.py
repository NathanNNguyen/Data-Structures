from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return int(self.size)

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         # check if empty list
#         if len(self.storage) == 0:
#             return None

#         self.size -= 1
#         return self.storage.pop()
        
# stack = Stack()
# print(len(stack))
# stack.push(2)
# stack.push(3)
# print(len(stack))
# print(f"removed value {stack.pop()}")

class Stack:
    def __init__(self):
        self.size = 0 
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # add an element to the front of the list
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        # check if empty
        if self.size == 0:
            return None

        # remove an element from the list
        # whatever we used to add to
        # it must be removing the same
        # add_to_head => remove_head
        # add_to_tail => remove_tail
        self.size -= 1
        return self.storage.remove_head()