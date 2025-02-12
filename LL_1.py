class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while (fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print(my_linked_list.find_middle_node().value)

#papildus risinājums

import re
myinput = input()
if (re.search("^-?\\d*(\\.\\d+)?$", myinput)):
    my_little_list = LinkedList(myinput)

    myinput = input()
    while (True):
        if not (re.search("^-?\\d*(\\.\\d+)?$", myinput)):
            print("tas nav skaitlis")
        my_little_list.append(myinput)
        myinput = input()

else:
    print("tas nav skaitlis")