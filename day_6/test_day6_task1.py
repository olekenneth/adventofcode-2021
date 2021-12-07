import unittest
from utils import readfile

class Test_Day6_Task1(unittest.TestCase):
    day = 0
    data = []

    def calc_age(self, age):
        if age == 0:
            self.data.append(9)
            age = 7
        return age - 1

    def day_tick(self):
        self.day += 1
        self.data = list(map(self.calc_age, self.data))


    def test(self):
        csv = readfile('./day_6/data.txt')
        self.data = list(map(int, csv[0].split(',')))
        while self.day < 80:
            #print('After ', self.day, self.data)
            self.day_tick()
        print('total fish', len(self.data))
        assert(len(self.data) == 346063)
