# FIFO ,first in first out
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
         
    def enqueue(self,value):
        new_node = Node(value)
        if self.front is None:
            self.front = self.rear = new_node
        else:
             self.rear.next = new_node
             self.rear = new_node 

        self.size += 1


 
    def dequeue(self):
        if self.front == None:
            print('Queue is empty')
        
        print(self.front.value)
        self.front = self.front.next

        if self.front == None:
            self.rear = None

        self.size -= 1

        
    
    def __printQueue__(self):
        item = []
        current_item = self.front
        while current_item is not None:
            item.append(str(current_item.value))
            current_item = current_item.next

        return print(item)
        

    def __len__(self):
        print(self.size)

    def peek(self):
        pass

if __name__ == "__main__":
    myqueue = Queue()
    myqueue.enqueue(7)
    myqueue.enqueue(11)
    myqueue.enqueue(13)
    myqueue.enqueue(17) 
    myqueue.enqueue(19)
    myqueue.enqueue(23)
    myqueue.enqueue(29)
    myqueue.__printQueue__()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.__printQueue__()
    myqueue.__len__()



    