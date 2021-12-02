import unittest
from utils import readlines

class Test3(unittest.TestCase):
    x = 0
    y = 0
    aim = 0

    def do_task(self, line):
        command, offset = line.split(' ')
        offset = int(offset)
        if command == 'forward':
            self.x += offset
            self.y += self.aim * offset
        if command == 'backward':
            self.x -= offset
            self.y -= self.aim * offset
        if command == 'down':
            self.aim += offset
        if command == 'up':
            self.aim -= offset

    def test_3(self):
        readlines('./day_2/data.txt', self.do_task)
        print('position', self.x, '/', self.y, '=', self.x * self.y)
        assert(self.x * self.y == 1813062561)
