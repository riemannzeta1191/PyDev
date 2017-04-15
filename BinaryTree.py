import sys
class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_data(self):
        return self.key

    def set_data(self, item):
        self.key = item

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insertLeft(self, data):
        if self:
            if self.left == None:
                self.left = BinaryTree(data)
            else:
                temp = BinaryTree(data)
                temp.left = self.left
                self.left = temp

    def insertRight(self, data):
        if self:
            if self.right == None:
                self.right = BinaryTree(data)
            else:
                temp = BinaryTree(data)
                temp.right = self.right
                self.right = temp




a = BinaryTree(6)
a.insertLeft(8)
b = a.insertRight(9)



print a.__dict__