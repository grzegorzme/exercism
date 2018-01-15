class Luhn(object):
    def __init__(self, number):
        self.number = str(number).replace(' ', '')

    def is_valid(self):
        print(self.number)
        if self.number.isdigit() and len(self.number) > 1:
            return (sum(2*int(x)-9 if int(x) > 4 else 2*int(x) for x in self.number[-2::-2]) +
                    sum(int(x) for x in self.number[-1::-2])) % 10 == 0
        else:
            return False
