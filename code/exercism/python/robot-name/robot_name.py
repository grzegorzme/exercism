import random
import string


class Robot(object):
    ROBOT_LIST = set()

    def __init__(self):
        self.name = None
        self.generate_name()

    def generate_name(self):
        random.seed()
        while True:
            new_name = ''.join([random.choice(string.ascii_uppercase) for _ in range(2)]) + \
                        str(random.randint(0, 1000)).ljust(3, '0')
            if new_name not in self.ROBOT_LIST:
                self.ROBOT_LIST.discard(self.name)
                self.name = new_name
                return

    def reset(self):
        self.generate_name()
