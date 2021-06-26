class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        if self.succeeding is not None:
            self.succeeding.previous = self
        self.previous = previous
        if self.previous is not None:
            self.previous.succeeding = self

    def __repr__(self):
        return f"{str(self.previous)}|{self.value}|{self.succeeding}"


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.len = 0

    def push(self, value):
        if self.len == 0:
            self.start = Node(value)
            self.end = self.start
        else:
            self.end = Node(value, previous=self.end)
        self.len += 1

    def pop(self):
        if self.len > 0:
            r = self.end
            self.end = r.previous
            self.len -= 1
            return r.value

    def shift(self):
        if self.len > 0:
            r = self.start
            self.start = r.succeeding
            self.len -= 1
            return r.value

    def unshift(self, value):
        if self.len == 0:
            self.start = Node(value)
            self.end = self.start
        else:
            self.start = Node(value, succeeding=self.start)
        self.len += 1

    def __repr__(self):
        return str(list(self))

    def __len__(self):
        return self.len

    def __iter__(self):
        current = self.start
        while current is not None:
            yield current.value
            current = current.succeeding
