from Linked_List import Node, SinglyLinkedList




def main():
    # Create a singly linked list
    my_list = SinglyLinkedList()

    # Insert nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # Connect nodes
    my_list.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("my list head : ",my_list.head)

    # Insert a new node at the end
    new_node = Node(6)
    my_list.insert_at_end(new_node)

    print(my_list.head)
    