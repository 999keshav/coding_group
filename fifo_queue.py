class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class fifo_queue:
    def __init__(self):
        self.link = None

    def put(self, data):
        node = Node(data)
        node.next = self.link
        self.link = node


    def get(self, index=0):
        _link = self.link
        while index > 0 :
            _link = _link.next
            index -= 1
        return _link.data

    def queue_length(self):
        _link = self.link
        count = 0
        while _link :
            count += 1
            _link = _link.next
        return count

    def is_empty(self):
        if not self.link:
            return True
        else:
            return self.queue_length()



a = fifo_queue()
a.put(5)
a.put(3)
a.put(6)
a.put(3)
a.put(1)
a.put(10)
a.put(57)
a.put(3)
a.put(8)
a.put(5)
a.put(3)
a.put(100)

b = fifo_queue()

print(a.queue_length())
print(a.get(5))

print(a.is_empty(),b.is_empty())
