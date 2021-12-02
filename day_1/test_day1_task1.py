import unittest
from utils import readlines

class Test1(unittest.TestCase):
    prev = False
    increased = 0

    def do_task(self, line):
        data = int(line)
        if self.prev != False and data > self.prev:
            self.increased += 1
            print(data, '(increased)')
        else:
            print(data, '(decreased)')
        self.prev = data

    def test_1(self):
        readlines('./day_1/data-1.txt', self.do_task)
        print('there are ', self.increased, ' measurements')
        assert(self.increased == 1451)
