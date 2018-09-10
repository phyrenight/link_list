from node import Node

class LinkList():
    def  __init__(self):
        self.head = None


    def add_item(self, item):
        new_item = Node(item)
        if(self.head):
            new_item.next_item = self.head
            self.head = new_item
        else:
            self.head = new_item


    def isEmpty(self):
        if(self.head):
            return False
        else:
            return True

