import unittest
from utils import readfile

class Test1(unittest.TestCase):
    index = 0
    prev = False
    increased = 0
    stack = []

    def finished(self, a_sum, b_sum):
        if a_sum > b_sum:
            self.increased += 1
            print(a_sum, '(increased)')
        else:
            print(b_sum, '(decreased)')

    def test_2(self):
        file = readfile('./day_1/data-1.txt')
        for i, data in enumerate(file):
            if i >= 2:
                self.stack.append(int(file[i - 2]) + int(file[i - 1]) + int(file[i]))

        for index,value  in enumerate(self.stack):
            if (index > 0):
                self.finished(value, self.stack[index - 1])

        print('there are ', self.increased, ' measurements')
        assert(self.increased == 1395)
