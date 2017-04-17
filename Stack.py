# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, item):
        self.data.append(item)
        self.size += 1

    def pop(self):
        return self.data.pop(0)

    def max(self):
        max = self.data[0]
        for item in range(len((self.data))):
            if max <= self.data[item]:
                max = self.data[item]
        return max

a = Stack()
a.push(8999999999999)
a.push(67)
a.push(59)
a.push(65756)
print a.max()
print a.__dict__