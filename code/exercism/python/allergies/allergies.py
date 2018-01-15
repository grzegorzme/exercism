class Allergies(object):

    allergenes = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats'
    }

    def __init__(self, score):
        self._lst = [self.allergenes[a] for a in [int(o)*2**i for i, o in enumerate(reversed('{0:b}'.format(score)))]
                     if a in self.allergenes]

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return self._lst
