class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(current, prev=None):
    if current is None:
        return prev
    next_node = current.next
    current.next = prev
    return reverse_linked_list(next_node, current)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
new_head = reverse_linked_list(head)

while new_head:
    print(new_head.data, end=" -> ")
    new_head = new_head.next
print("None")