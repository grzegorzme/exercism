class BufferFullException(Exception):
    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(Exception):
    def __init__(self, message):
        super().__init__(message)


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def write(self, x, force=False):
        if len(self.buffer) >= self.capacity:
            if force:
                self.buffer = self.buffer[1:] + [x]
            else:
                raise BufferFullException('buffer full')
        else:
            self.buffer.append(x)

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException('buffer empty')
        else:
            x = self.buffer[0]
            self.buffer = self.buffer[1:]
            return x

    def overwrite(self, x):
        self.write(x, force=True)

    def clear(self):
        self.buffer = []
