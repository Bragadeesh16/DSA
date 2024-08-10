class Stack:
    def __init__(self) -> None:
        self.stack = list()

    def addtostack(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False
    def removes(self):
        if len(self.stack) > 0 :
            self.stack.pop()
        else:
            print('there is no element in the stack')

    def size(self):
        print(len(self.stack))

stack = Stack()
stack.addtostack(3)
stack.addtostack(4)
stack.addtostack(5)
stack.addtostack(6)
print(stack.stack)
stack.removes()
print(stack.stack)