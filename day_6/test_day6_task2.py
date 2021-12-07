import unittest
from utils import readfile
from collections import Counter

class Test_Day6_Task2(unittest.TestCase):
    day = 0
    data = []

    def calc_age(self, age):
        if age == 0:
            self.data.append(9)
            age = 7
        return age - 1

    def day_tick(self):
        self.day += 1
        subtrack_counter = Counter({ 1:1, 2:1, 3:1, 4:1, 5: 1})
        self.data.subtract(subtrack_counter)


    def test(self):
        csv = readfile('./day_6/data-small.txt')
        self.data = Counter(list(map(int, csv[0].split(','))))
        print(self.data)
        self.day_tick()
        print(self.data)

        # while self.day < 80:
        #     #print('After ', self.day, self.data)
        #     self.day_tick()
        print('total fish', len(self.data))
        assert(0 == 0)
