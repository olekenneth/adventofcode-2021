import unittest
from utils import readfile
from collections import Counter

class Test_Day6_Task2(unittest.TestCase):
    data = []
    counter = {}
    fuel = []

    def calc_fuel(self, x):
        fuel = 0
        for key in self.data:
            fuel += abs(key - x) * self.data[key]
        self.fuel.append(fuel)
        return fuel

    def test(self):
        csv = readfile('./day_7/data.txt')
        self.counter = Counter(list(map(int, csv[0].split(','))))
        self.data = dict(self.counter)
        most_common = self.counter.most_common(3)
        commons = [most_common[0][0], most_common[1][0], most_common[2][0]]
        i = 0
        while i < max(self.data):
            self.calc_fuel(i)
            i += 1
        assert(min(self.fuel) == 341534)
