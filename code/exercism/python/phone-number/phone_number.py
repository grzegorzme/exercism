class Phone(object):
    def __init__(self, phone_number):
        self.number = self.cleanup(phone_number)
        self.area_code = self.number[0:3]

    @staticmethod
    def cleanup(phone_number):
        output = ''.join(c for c in str(phone_number) if c.isdigit())
        if (len(output) == 11 and output[0] == '1') or len(output) == 10:
            output = output[-10:]
            if int(output[0]) > 1 and int(output[3]) > 1:
                return output

        raise ValueError('invalid phone number')

    def pretty(self):
        return '({}) {}-{}'.format(self.number[0:3], self.number[3:6], self.number[6:10])
