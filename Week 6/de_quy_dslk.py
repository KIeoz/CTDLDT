class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(current):
    if current is None:
        return
    print(current.data, end=" -> ")
    print_linked_list(current.next)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print_linked_list(head)
print("None")
