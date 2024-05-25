class node: #creating a new node
    def __init__(self,x) -> None:
        self.item = x
        self.next = None

class linked_list:
    def __init__(self) -> None:
        self.head = None # define the head

    def head_node(self,data):
        new_node = node(data) 
        if self.head == None:
            self.head = new_node
            print(self.head)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_elements(self):
        current = self.head
        while current:
            print(current.item)
            current = current.next
        print('null')

    def add_at_front(self,data):
        new_node = node(data)
        temp = self.head
        new_node.next = temp
        self.head = new_node

    def search(self,key):
        temp = self.head
        found = False
        while (found == False):
            if temp.item == key:
                found = True
            else:
                found = False
            temp = temp.next
        if found:
            print('the element is found')
        else:
            print('the element is not found')

    def reverse_linedList(self):
        temp = self.head
        prev = None
        front = None
        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        print(prev)

    def sortList(self):
        pointer_one = self.head
        pointer_two = self.head.next
        current = None
        
        
        if pointer_one == 0:
            return 0
        
        while pointer_one:
            print(pointer_one.item)
            while pointer_two:
                print(pointer_two.ne)
                if pointer_one.item < pointer_two.item:
                    temp = pointer_two
                    temp.next = current
                    current = temp
                    
                pointer_two = pointer_two.next
                
            pointer_one = pointer_one.next
            
        return current


lists = linked_list()
lists.head_node(1)
lists.head_node(6)
lists.head_node(2)
lists.head_node(2)
lists.head_node(1)
lists.add_at_front(9)
lists.search(2)
lists.sortList()
lists.print_elements()