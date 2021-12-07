import unittest
from statistics import mode
from utils import readfile

class Test_Day3_Task1(unittest.TestCase):
    gamma = 0
    epsilon = 0
    common_bits = []

    def find_common(self, bits):
        self.common_bits.append(mode(bits))

    def do_task(self, line):
        self.data.append(list(line))

    def test(self):
        rows = readfile('./day_3/data.txt')
        cols = list(map(lambda x: [], list(rows[0])))
        for line in rows:
            for i, bit in enumerate(list(line)):
                cols[i].append(bit)
        for r in cols:
            self.find_common(r)

        self.gamma = int(''.join(self.common_bits).encode(), 2)
        self.epsilon = int(''.join(['1' if i == '0' else '0'
                                    for i in self.common_bits]).encode(), 2)

        print('gamma/epsilon rate', self.gamma, '*', self.epsilon, '=', self.gamma * self.epsilon)
        assert(self.gamma * self.epsilon == 2035764)
