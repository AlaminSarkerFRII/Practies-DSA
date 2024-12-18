
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initialize next as None (no node connected yet)  # Node is a class which contains data and next node reference.


# Single Linked list

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, node):
        if not self.head:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        
 
 
        
    
        
 