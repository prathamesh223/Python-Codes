class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            return
        l=self.head
        while l.next!=None:
            l=l.next
        l.next=new_node
    def display(self):
        d=self.head
        while d!=None:
            print(d.data)
            d=d.next
    # def delete(self,key):
    #     temp=self.head
    #     if temp is not None:
    #         if temp.data == key:
    #             self.head=temp.next
    #             temp=None
    #             return
    #         whi

# l=LinkedList()
# l.append(1)
# l.append(2)
# l.append(3) 
# l.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def append(self,item):
        new_node=Node(item)
        if self.head==None:
            self.head=new_node
            return
        l=self.head
        while l.next!=None:
            l=l.next

        l.next=new_node
    def display(self):
        d=self.head
        while d!=None :
            print(d.data)
            d=d.next
l1=Linked_list()
l1.append("A")
l1.append("B")
l1.append("c")
l1.display()


