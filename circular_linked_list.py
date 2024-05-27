class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class circular_linked_list:
    def __init__(self) -> None:
        self.head = None

    def add_node(self,data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

