class Node(object):
    def __init__(self,value = None,next = None):
        self.value =  value
        self.next =  next

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node


    def insert_end(self, data):
        new_node = Node(data)
        new_node.set_next(None)



    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() ==data:
                found = True
            else:
                current = current.get_next()
        return current

    def delete(self, data):
        current = self.head
        found = False
        previous = None
        if current and found == False:
            current = current.get_next()
        else:
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())






