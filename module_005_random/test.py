import unittest
import main
from test_utils import *


class TestModule5(unittest.TestCase):
    times = 300000

    def assertInBounds(self, lo, arg, hi):
        self.assertGreaterEqual(arg, lo)
        self.assertLessEqual(arg, hi)

    @random_test(True, times)
    def random_test_1(self, lower, upper, arg1, arg2):
        return lower < main.task_1(arg1, arg2) < upper

    def test_task_1(self):
        self.assertInBounds(self.times * 0.009, self.random_test_1(19, 20.5, 20, 70), self.times * 0.011)
        self.assertInBounds(self.times * 0.019, self.random_test_1(55, 56, 20, 70), self.times * 0.021)
        self.assertInBounds(self.times * 0.79, self.random_test_1(-40, 40, -50, 50), self.times * 0.81)
        self.assertInBounds(self.times * 0.045, self.random_test_1(40, 45, -50, 50), self.times * 0.055)
        self.assertInBounds(self.times * 0.079, self.random_test_1(-40, 40, -500, 500), self.times * 0.081)
        self.assertInBounds(self.times * 0.079, self.random_test_1(-4, 4, -50, 50), self.times * 0.081)
        self.assertInBounds(self.times, self.random_test_1(-60, 60, -50, 50), self.times)
        self.assertInBounds(0, self.random_test_1(70, 71, 20, 70), 0)
