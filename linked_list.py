class LinkedListNode:
    def __init__(self, data, next =None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head):
        self.head = head

    def __len__(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next

        return counter

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def push(self,data):
        new_node=LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self,data,prev_node):
        new_node=LinkedListNode(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def append(self,data):
        new_node=LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            return
        node=self.head
        while node.next:
            node=node.next
        node.next = new_node


