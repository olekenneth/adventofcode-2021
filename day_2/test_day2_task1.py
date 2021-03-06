import unittest
from utils import readlines

class Test3(unittest.TestCase):
    x = 0
    y = 0

    def do_task(self, line):
        command, offset = line.split(' ')
        offset = int(offset)
        if command == 'forward':
            self.x += offset
        if command == 'backward':
            self.x -= offset
        if command == 'down':
            self.y += offset
        if command == 'up':
            self.y -= offset

    def test_3(self):
        readlines('./day_2/data.txt', self.do_task)
        print('position', self.x, '/', self.y, '=', self.x * self.y)
        assert(self.x * self.y == 1947824)
        assert(self.x == 1817)
        assert(self.y == 1072)
