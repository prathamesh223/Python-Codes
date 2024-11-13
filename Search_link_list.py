class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def search(self,key):
        current_node=self.head
        while current_node:
            if current_node.data==key:
                return True
            current_node=current_node.next
        return False
    def print_list(self):
        current_node=self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
llist=Linkedlist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
print(llist.search("C"))
print(llist.search("E"))
print(llist.print_list())