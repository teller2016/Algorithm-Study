class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.input = None
        self.output = None

    def push(self, item):
        self.input = Node(item, self.input)

    def pop(self):
        self.move()
        if self.output is None:
            print("EMPTY")
            return None
        item = self.output.item
        self.output = self.output.next
        return item

    def move(self):
        if self.output is None:
            while self.input:
                self.output = Node(self.input.item, self.output)
                self.input = self.input.next

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())

queue.push(4)
print(queue.pop())