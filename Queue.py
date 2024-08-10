class Queue:
    def __init__(self) -> None:
        self.queue = list()

    def addtoq(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    
    def size(self):
        return len(self.queue)
    
    def removeq(self):
        if len(self.queue) > 0:
            self.queue.pop()
        else:
            print('there is no element in queue')

queue = Queue()
queue.addtoq(1)
queue.addtoq(1)
queue.addtoq(2)
queue.addtoq(1)
queue.removeq()
queue.removeq()
queue.removeq()
print(queue.size())