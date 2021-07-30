class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
         #print("No previous node exist in the Linkedlist")
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert(self,prev_node,data=None):
        new_node=Node(data)
        if not prev_node:
            return
        new_node.next=prev_node.next
        prev_node.next=new_node

    def delete(self,key):
        cur_node=self.head
        if cur_node and cur_node.data==key:
            self.head=cur_node.next
            cur_node=None
            return
        prev=None
        while cur_node and cur_node.data!=key:
            prev=cur_node
            cur_node=cur_node.next
        if cur_node is None:
            return
        prev.next=cur_node.next
        cur_node=None

    def delete_p(self,pos):
        cur_node=self.head
        if pos==0:
            self.head=cur_node.next
            cur_node=None
            return

        prev = None
        cur_node = self.head.next
        count=0
        while cur_node and cur_node!=pos:
            prev=cur_node
            cur_node=cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def swap_node(self, key1, key2):
        if key1==key2:
            return
        prev_1=None
        cur_1=self.head
        while cur_1 and cur_1.data!=key1:
            prev_1=cur_1
            cur_1=cur_1.next
        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key2:
            prev_2 = cur_2
            cur_2 = cur_2.next
        if not cur_1 or not cur_2:
            return
        if prev_1:
            prev_1.next=cur_2
        else:
            self.head=cur_2
        if prev_2:
            prev_2.next=cur_1
        else:
            self.head=cur_1

        cur_1.next,cur_2.next=cur_2.next,cur_1.next


a=LinkedList()
a.append("A")
a.append("B")
a.append("C")
a.append("D")
a.insert(a.head.next, "E")
#a.prepend("E")
#a.delete("A")
a.delete_p(1)
#a.swap_list("B","C")
a.print_list()

