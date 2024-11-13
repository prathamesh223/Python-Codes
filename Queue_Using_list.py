class Queue:
    def __init__(self, capacity):
        self.queue=[None]*capacity
        self.rear=-1
        self.front=0
        self.capacity=capacity
        self.size=0
    def enqueue(self,item):
        if self.isfull():
            print("Queue is full")
            return
        self.rear=(self.rear+1)%self.capacity
        self.queue[self.rear]=item
        self.size+=1
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        item=self.queue[self.front]
        self.front=(self.front + 1) % self.capacity
        self.size-=1
        return item
    def isfull(self):
        return self.size==self.capacity
    def isempty(self):
        return self.size==0
    def display(self):
        for i in range(self.size):
            print(self.queue[(self.front+i)%self.capacity])
    def peek(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.queue[self.front]
# obj=Queue(3)
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.display()
# print(obj.peek())
    
class Queue1:
    def __init__(self,capacity):
        self.queue=[None]*capacity
        self.rear=-1
        self.front=0
        self.size=0
        self.capacity=capacity
    def enqueue(self,item):
        if self.isfull():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear]=item
        self.size+=1
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        item=self.queue[self.front]
        self.front = (self.front + 1) % self.capacity

        self.size-=1
        return item
    def isfull(self):
        return self.size==self.capacity
    def  isempty(self):
        return self.size==0
    def peek(self):
        if self.isempty():
            print("Queue is empty")
            return 
        return self.queue[self.front]
    def display(self):
        for i in range(len(self.queue)):
            print(self.queue[(self.front + i) % self.capacity])
    
o=Queue1(4)
o.enqueue(1)
o.enqueue(2)
o.enqueue(3)
o.enqueue(4)
print(o.display())
# o.dequeue()
# print(o.peek())
print(o.peek())
