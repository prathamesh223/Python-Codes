# class Stack:
#     def __init__(self,capacity):
#         self.stack=[None]*capacity
#         self.top=-1
#         self.size=0
#         self.capacity=capacity
#     def push(self,item):
#         if self.isfull():
#             print("Stack is full")
#             return
#         self.top+=1
#         self.stack[self.top]=item
#         self.size+=1
#     def pop(self):
#         if self.isempty():
#             print("Stack is empty")
#             return 
#         item=self.stack[top]
#         self.top-=1
#         self.size-=1
#         return item
#     def isfull(self):
#         return self.size==self.capacity
#     def isempty(self):
#         return self.size==0
#     def peek(self):
#         if self.isempty():
#             print("Stack is empty")
#             return
#         return self.stack[self.top]
#     def display(self):
#         for i in range(self.size):
#             print(self.stack[i])
# obj=Stack(3)
# obj.push(1)
# obj.push(2)
# obj.push(3)
# # obj.display()
# print(obj.peek())

class Stack1:
    def __init__(self,cap):
        self.stack=[None]*cap
        self.top=-1
        self.size=0
        self.cap=cap
    def push(self,item):
        if self.isfull():
            print("Stack is full")
            return
        self.top+=1
        self.stack[self.top]=item
        self.size+=1
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return 
        item=self.stack[self.top]
        self.top-=1
        self.size-=1
        return item
    def isfull(self):
        return self.size==self.cap
    def isempty(self):
        return self.size==0
    def peek(self):
        if self.isempty():
            print("Stack is empty")
            return 
        return self.stack[self.top]
    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])
s=Stack1(4)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
print(s.pop())
print(s.peek())
