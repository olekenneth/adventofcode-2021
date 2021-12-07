import unittest
from utils import readfile
from collections import Counter

class Test_Day6_Task2(unittest.TestCase):
    day = 0
    data = []
    counter = {}
    prev_round = 0

    def day_tick(self):
        self.day += 1
        self.prev_round = self.counter['0']

        self.counter = Counter({
            '0': self.counter['1'],
            '1': self.counter['2'],
            '2': self.counter['3'],
            '3': self.counter['4'],
            '4': self.counter['5'],
            '5': self.counter['6'],
            '6': self.counter['7'] + self.prev_round,
            '7': self.counter['8'],
            '8': self.prev_round,
        })

    def test(self):
        csv = readfile('./day_6/data.txt')
        self.data = list(map(str, csv[0].split(',')))
        self.counter = Counter(self.data)

        while self.day < 256:
            #print('After ', self.day, dict(self.counter))
            self.day_tick()

        total = 0
        for d in self.counter:
            print(d, self.counter[d])
            total += 1 * self.counter[d]

        print('total', total)
        assert(total == 1572358335990)
