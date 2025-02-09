from node import Node
from copy import copy, deepcopy

class LinkedList:

    def __init__(self, element):
        self.node = Node(element)

    def append(self, element):

        current_node = self.node
        next_node = current_node.next
        while True:
            if next_node == None:
                next_node = Node(element)
                break;
            else:
                current_node = next_node;

    def traverse(self):

        current_node = deepcopy(self.node)
        while True:
            print(self.node)
            if self.node.next == None:
                break
            else:
                self.node = self.node.next

ll = LinkedList(1)

for i in range(5):
    ll.append(int(i + 2))

ll.traverse()
