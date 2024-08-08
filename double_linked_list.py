class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self) -> None:
        self.head = None

    def add_node(self,data):
        new_node = node(data)

        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

    def reverse_print(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.prev,end=' <- ')
            temp = temp.prev

