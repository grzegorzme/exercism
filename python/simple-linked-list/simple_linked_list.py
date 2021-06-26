class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def __next__(self):
        return self._next

    def next(self):
        return self.__next__()


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._len = 0

        for value in values:
            self.push(value=value)

    def __len__(self):
        return self._len

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = next(current)

    def head(self):
        if self._head is None:
            raise EmptyListException("empty list")
        return self._head

    def push(self, value):
        self._head = Node(value=value, next=self._head)
        self._len += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("empty list")
        else:
            out, self._head, self._len = self._head, next(self._head), self._len - 1
            return out.value()

    def reversed(self):
        return reversed(list(self))


class EmptyListException(Exception):
    pass
