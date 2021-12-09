import unittest
from utils import readfile
from collections import Counter

class Test_Day9_Task1(unittest.TestCase):
    risk_level = 0
    file = []
    def is_lowest(self, i, j, num):
        adjecent = []
        if i > 0:
            adjecent.append(self.file[i - 1][j]) # up
        if i < len(self.file) - 1:
            adjecent.append(self.file[i + 1][j]) # down
        if j > 0:
            adjecent.append(self.file[i][j - 1]) # left
        if j < len(self.file[i]) - 1:
            adjecent.append(self.file[i][j + 1]) # right
        return all(num < i for i in adjecent)

    def test(self):
        self.file = list(map(lambda x: list(map(int, list(x))), readfile('./day_9/data.txt')))

        for i, line in enumerate(self.file):
            for j, num in enumerate(line):
                if self.is_lowest(i, j, num):
                    self.risk_level += num + 1
        assert(self.risk_level == 524)
