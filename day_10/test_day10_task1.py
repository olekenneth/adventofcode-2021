import unittest
from utils import readfile

class TestDay10task1(unittest.TestCase):
    mapping = {
        ']': '[',
        '}': '{',
        '>': '<',
        ')': '(',
        '[': ']',
        '{': '}',
        '<': '>',
        '(': ')',
    }

    points_mapping = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    tags = []
    points = 0

    def test(self):
        data = readfile('./day_10/data.txt')

        open_tags = list(self.mapping.values())[:4]
        close_tags = list(self.mapping.keys())[:4]
        for line in data:
            chars = list(line)
            self.tags = []
            for char in chars:
                if char in open_tags:
                    self.tags.append(char)
                if char in close_tags:
                    if self.mapping[char] == self.tags[-1:][0]:
                        self.tags.pop()
                    else:
                        print(''.join(self.tags), 'expected', self.mapping[self.tags[-1:][0]], 'Found', char)
                        self.points += self.points_mapping[char]
                        break
        assert(self.points == 321237)
