class Node():
    def __init__(self, item, next_item=None):
        self.item = item
        self.next_item = next_item


    def get_item(self):
        return self.item


    def set_next_item(self, next_item):
        self.next_item = next_item