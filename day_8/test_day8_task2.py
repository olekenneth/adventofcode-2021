import unittest
from utils import readlines

length_to_segments = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

letters_to_segments = {
}

class Test_Day8_Task2(unittest.TestCase):
    data = 0
    counter = {}

    def find_num(self, signals, nums):
        mapping = {}
        out = []
        for num in signals:
            num_len = len(num)
            if num_len in length_to_segments:
                actual_num = length_to_segments[num_len]
                mapping[actual_num] = list(num)

        for num in nums:
            num_len = len(num)
            if num_len in length_to_segments:
                actual_num = length_to_segments[num_len]
                out.append(actual_num)
            if len(num) == 6: # 0,6,9
                if set(mapping[4]).issubset(list(num)):
                    out.append(9)
                    mapping[9] = list(num)
                else:
                    if set(mapping[7]).issubset(list(num)):
                        out.append(0)
                    else:
                        out.append(6)
                        mapping[6] = list(num)
            elif len(num) == 5: # 2,3,5
                if set(mapping[7]).issubset(list(num)):
                    out.append(3)
                    mapping[3] = list(num)
                else:
                    if set(set(mapping[4]) - set(mapping[1])).issubset(list(num)):
                        out.append(5)
                    else:
                        out.append(2)

        out = list(map(str, out))
        self.data += int(''.join(out))

    def readline(self, line):
        signals = line.split('|')[0].strip().split(' ')
        nums = line.split('|')[1].strip().split(' ')
        self.find_num(signals, nums)

    def test(self):
        readlines('./day_8/data.txt', self.readline)
        print(self.data)

        assert(self.data == 994266)
