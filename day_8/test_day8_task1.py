import unittest
from utils import readlines
from collections import Counter

length_to_segments = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

class Test_Day8_Task1(unittest.TestCase):
    data = 0
    counter = {}

    def count(self, num):
        print('num', num)
        if num in length_to_segments:
            self.data += 1

    def readline(self, line):
        list(map(self.count, map(len, line.split('|')[1].strip().split(' '))))

    def test(self):
        readlines('./day_8/data.txt', self.readline)
        print(self.data)

        assert(self.data == 543)
