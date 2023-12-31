import unittest
import main


class TestModule0(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(1044, main.task_1(36, 29))
        self.assertEqual(4700, main.task_1(-100, -47))
        self.assertEqual(66, main.task_1(64, 2))
        self.assertEqual(435, main.task_1(-5, -87))
        self.assertEqual(-172, main.task_1(-43, 4))
        self.assertEqual(-3330, main.task_1(-37, 90))
        self.assertEqual(-3950, main.task_1(50, -79))
        self.assertEqual(-5658, main.task_1(82, -69))
        self.assertEqual(-117, main.task_1(13, -9))
        self.assertEqual(897, main.task_1(69, 13))
        self.assertEqual(-90, main.task_1(18, -5))
        self.assertEqual(3995, main.task_1(85, 47))
        self.assertEqual(-4698, main.task_1(-87, 54))
        self.assertEqual(1134, main.task_1(54, 21))
        self.assertEqual(-2544, main.task_1(-53, 48))
        self.assertEqual(-204, main.task_1(12, -17))
        self.assertEqual(3720, main.task_1(-40, -93))
        self.assertEqual(5670, main.task_1(-90, -63))
        self.assertEqual(544, main.task_1(32, 17))
        self.assertEqual(-2139, main.task_1(23, -93))
        self.assertEqual(204, main.task_1(-17, -12))
        self.assertEqual(-2162, main.task_1(-94, 23))
        self.assertEqual(2709, main.task_1(63, 43))
        self.assertEqual(-1856, main.task_1(29, -64))
        self.assertEqual(2117, main.task_1(-73, -29))
        self.assertEqual(134, main.task_1(2, 67))
        self.assertEqual(2574, main.task_1(-78, -33))
        self.assertEqual(1071, main.task_1(51, 21))
        self.assertEqual(-324, main.task_1(4, -81))
        self.assertEqual(-2257, main.task_1(-37, 61))
        # handwritten cases
        self.assertEqual(0, main.task_1(0, 0))
        self.assertEqual(31, main.task_1(0, 31))
        self.assertEqual(10, main.task_1(10, 0))
        self.assertEqual(-40, main.task_1(-10, -30))
        self.assertEqual(-20, main.task_1(10, -30))
        self.assertEqual(20, main.task_1(-10, 30))

    def test_task_2(self):
        self.assertEqual('', main.task_2(28))
        self.assertEqual('', main.task_2(-79))
        self.assertEqual('', main.task_2(98))
        self.assertEqual('', main.task_2(91))
        self.assertEqual('fizz', main.task_2(-63))
        self.assertEqual('fizz', main.task_2(-93))
        self.assertEqual('fizzbuzz', main.task_2(15))
        self.assertEqual('', main.task_2(8))
        self.assertEqual('fizz', main.task_2(33))
        self.assertEqual('fizz', main.task_2(96))
        self.assertEqual('', main.task_2(-19))
        self.assertEqual('', main.task_2(-47))
        self.assertEqual('', main.task_2(73))
        self.assertEqual('fizz', main.task_2(-93))
        self.assertEqual('', main.task_2(-77))
        self.assertEqual('', main.task_2(89))
        self.assertEqual('buzz', main.task_2(55))
        self.assertEqual('', main.task_2(37))
        self.assertEqual('fizz', main.task_2(-33))
        self.assertEqual('buzz', main.task_2(95))
        self.assertEqual('', main.task_2(59))
        self.assertEqual('fizzbuzz', main.task_2(60))
        self.assertEqual('buzz', main.task_2(-100))
        self.assertEqual('', main.task_2(79))
        self.assertEqual('', main.task_2(-74))
        self.assertEqual('', main.task_2(13))
        self.assertEqual('', main.task_2(-7))
        self.assertEqual('', main.task_2(67))
        self.assertEqual('', main.task_2(47))
        self.assertEqual('buzz', main.task_2(-10))

    def test_task_3(self):
        self.assertEqual(-1, main.task_3(42, -3))
        self.assertEqual(36.49657518178932, main.task_3(6, 36))
        self.assertEqual(22.80350850198276, main.task_3(18, 14))
        self.assertEqual(19.235384061671343, main.task_3(17, 9))
        self.assertEqual(-1, main.task_3(13, -1))
        self.assertEqual(-1, main.task_3(50, -4))
        self.assertEqual(20.12461179749811, main.task_3(9, 18))
        self.assertEqual(50.11985634456667, main.task_3(24, 44))
        self.assertEqual(-1, main.task_3(24, -1))
        self.assertEqual(-1, main.task_3(7, -1))
        self.assertEqual(-1, main.task_3(0, 39))
        self.assertEqual(9.219544457292887, main.task_3(6, 7))
        self.assertEqual(44.68780594300866, main.task_3(29, 34))
        self.assertEqual(61.84658438426491, main.task_3(39, 48))
        self.assertEqual(-1, main.task_3(31, -2))
        self.assertEqual(43.829214001622255, main.task_3(25, 36))
        self.assertEqual(48.84669896727925, main.task_3(45, 19))
        self.assertEqual(45.89117562233506, main.task_3(9, 45))
        self.assertEqual(51.10772935672255, main.task_3(44, 26))
        self.assertEqual(47.80167361086848, main.task_3(13, 46))
        self.assertEqual(43.41658669218482, main.task_3(11, 42))
        self.assertEqual(7.615773105863909, main.task_3(3, 7))
        self.assertEqual(48.30113870293329, main.task_3(43, 22))
        self.assertEqual(59.90826320300064, main.task_3(50, 33))
        self.assertEqual(51.62363799656123, main.task_3(44, 27))
        self.assertEqual(50.774009099144415, main.task_3(43, 27))
        self.assertEqual(63.41135544995076, main.task_3(50, 39))
        self.assertEqual(45.5411901469428, main.task_3(45, 7))
        self.assertEqual(21.840329667841555, main.task_3(6, 21))
        self.assertEqual(-1, main.task_3(-4, 42))
        self.assertEqual(37.8021163428716, main.task_3(23, 30))
        self.assertEqual(-1, main.task_3(13, -3))
        self.assertEqual(20.12461179749811, main.task_3(9, 18))
        self.assertEqual(36.069377593742864, main.task_3(26, 25))
        self.assertEqual(-1, main.task_3(-1, 0))
        self.assertEqual(60.108235708594876, main.task_3(42, 43))
        self.assertEqual(-1, main.task_3(25, -2))
        self.assertEqual(-1, main.task_3(49, -2))
        self.assertEqual(19.235384061671343, main.task_3(9, 17))
        self.assertEqual(-1, main.task_3(-1, 44))
    def test_task_4(self):
        self.assertEqual(1, main.task_4(1))
        self.assertEqual(-1, main.task_4(-1))
        self.assertEqual(479001600, main.task_4(12))
        self.assertEqual(2, main.task_4(2))
        self.assertEqual(40320, main.task_4(8))
        self.assertEqual(362880, main.task_4(9))
        self.assertEqual(-1, main.task_4(-2))
        self.assertEqual(39916800, main.task_4(11))
        self.assertEqual(3628800, main.task_4(10))
        self.assertEqual(-1, main.task_4(-2))
        self.assertEqual(720, main.task_4(6))
        self.assertEqual(2, main.task_4(2))
        self.assertEqual(5040, main.task_4(7))
        self.assertEqual(6, main.task_4(3))
        self.assertEqual(479001600, main.task_4(12))

    def test_task_5(self):
        self.assertEqual(483, main.task_5(33, 13))
        self.assertEqual(-1062, main.task_5(11, -47))
        self.assertEqual(-559, main.task_5(-49, -37))
        self.assertEqual(-819, main.task_5(-40, -2))
        self.assertEqual(83, main.task_5(-40, 42))
        self.assertEqual(143, main.task_5(18, 8))
        self.assertEqual(408, main.task_5(16, 32))
        self.assertEqual(-123, main.task_5(-40, -42))
        self.assertEqual(594, main.task_5(9, 35))
        self.assertEqual(546, main.task_5(-15, 36))
        self.assertEqual(-287, main.task_5(-27, 13))
        self.assertEqual(595, main.task_5(-26, 43))
        self.assertEqual(34, main.task_5(10, 7))
        self.assertEqual(950, main.task_5(26, 50))
        self.assertEqual(820, main.task_5(40, 1))
        self.assertEqual(-1072, main.task_5(-18, -49))
        self.assertEqual(-506, main.task_5(-33, 10))
        self.assertEqual(-35, main.task_5(16, -18))
        self.assertEqual(-108, main.task_5(-17, 9))
        self.assertEqual(52, main.task_5(3, 10))
        self.assertEqual(348, main.task_5(40, 47))
        self.assertEqual(-550, main.task_5(9, -34))
        self.assertEqual(185, main.task_5(-13, 23))
        self.assertEqual(357, main.task_5(13, 29))
        self.assertEqual(-405, main.task_5(-41, -49))
        self.assertEqual(-627, main.task_5(17, -39))
        self.assertEqual(-187, main.task_5(11, -22))
        self.assertEqual(-612, main.task_5(-37, 13))
        self.assertEqual(-161, main.task_5(-20, -26))
        self.assertEqual(-230, main.task_5(1, -21))
        self.assertEqual(961, main.task_5(-15, 46))
        self.assertEqual(325, main.task_5(-27, 37))
        self.assertEqual(-75, main.task_5(12, -17))
        self.assertEqual(-285, main.task_5(-33, -24))
        self.assertEqual(918, main.task_5(47, 21))
        self.assertEqual(-150, main.task_5(-17, 2))
        self.assertEqual(-40, main.task_5(-6, -10))
        self.assertEqual(-232, main.task_5(-22, 6))
        self.assertEqual(945, main.task_5(43, -1))
        self.assertEqual(546, main.task_5(-15, 36))
        self.assertEqual(465, main.task_5(24, 38))
        self.assertEqual(-1125, main.task_5(-3, -47))
        self.assertEqual(-49, main.task_5(48, -49))
        self.assertEqual(-210, main.task_5(-1, -20))
        self.assertEqual(-190, main.task_5(-19, -1))
        self.assertEqual(245, main.task_5(29, 20))
        self.assertEqual(891, main.task_5(43, -10))
        self.assertEqual(253, main.task_5(22, 0))
        self.assertEqual(-476, main.task_5(-36, -20))
        self.assertEqual(-81, main.task_5(-13, -5))
    def test_task_6(self):
        self.assertEqual(24638, main.task_6(71, 41, 84))
        self.assertEqual(20722, main.task_6(43, 67, 68))
        self.assertEqual(0, main.task_6(50, 6, -3))
        self.assertEqual(9172, main.task_6(32, 23, 70))
        self.assertEqual(17468, main.task_6(14, 81, 80))
        self.assertEqual(7398, main.task_6(77, 39, 6))
        self.assertEqual(16516, main.task_6(35, 74, 52))
        self.assertEqual(2822, main.task_6(13, 66, 7))
        self.assertEqual(23200, main.task_6(20, 80, 100))
        self.assertEqual(33204, main.task_6(92, 74, 59))
        self.assertEqual(41646, main.task_6(95, 69, 87))
        self.assertEqual(4048, main.task_6(16, 14, 60))
        self.assertEqual(26288, main.task_6(46, 63, 94))
        self.assertEqual(2246, main.task_6(34, 9, 19))
        self.assertEqual(12970, main.task_6(65, 5, 88))
        self.assertEqual(6600, main.task_6(22, 64, 22))
        self.assertEqual(23084, main.task_6(36, 62, 95))
        self.assertEqual(6088, main.task_6(14, 31, 58))
        self.assertEqual(19516, main.task_6(26, 85, 68))
        self.assertEqual(17992, main.task_6(58, 62, 45))
        self.assertEqual(23518, main.task_6(49, 71, 69))
        self.assertEqual(21848, main.task_6(42, 62, 80))
        self.assertEqual(4540, main.task_6(40, 5, 46))
        self.assertEqual(750, main.task_6(7, 1, 46))
        self.assertEqual(13134, main.task_6(69, 27, 49))
        self.assertEqual(50094, main.task_6(99, 99, 77))
        self.assertEqual(6554, main.task_6(85, 4, 33))
        self.assertEqual(0, main.task_6(87, -3, 74))
        self.assertEqual(6790, main.task_6(34, 89, 3))
        self.assertEqual(11352, main.task_6(36, 48, 47))
        self.assertEqual(2216, main.task_6(38, 6, 20))
        self.assertEqual(11644, main.task_6(88, 31, 26))
        self.assertEqual(19584, main.task_6(33, 84, 60))
        self.assertEqual(22622, main.task_6(31, 87, 73))
        self.assertEqual(0, main.task_6(52, -1, 70))
        self.assertEqual(14166, main.task_6(97, 27, 36))
        self.assertEqual(7320, main.task_6(78, 38, 6))
        self.assertEqual(14720, main.task_6(100, 12, 55))
        self.assertEqual(3336, main.task_6(24, 9, 44))
        self.assertEqual(7010, main.task_6(29, 77, 12))
        self.assertEqual(19438, main.task_6(58, 31, 89))
        self.assertEqual(0, main.task_6(36, -4, -5))
        self.assertEqual(2428, main.task_6(10, 8, 63))
        self.assertEqual(0, main.task_6(62, -1, 25))
        self.assertEqual(12462, main.task_6(75, 3, 77))
        self.assertEqual(56800, main.task_6(100, 92, 100))
        self.assertEqual(26292, main.task_6(32, 77, 98))
        self.assertEqual(10614, main.task_6(57, 35, 36))
        self.assertEqual(15126, main.task_6(45, 23, 96))
        self.assertEqual(21958, main.task_6(100, 89, 11))
    def test_task_7(self):
        self.assertEqual(True, main.task_7(71, 28, 49))
        self.assertEqual(False, main.task_7(34, 16, 2))
        self.assertEqual(False, main.task_7(11, 68, 17))
        self.assertEqual(False, main.task_7(29, 15, 83))
        self.assertEqual(False, main.task_7(55, 31, 19))
        self.assertEqual(True, main.task_7(65, 51, 84))
        self.assertEqual(False, main.task_7(61, 94, 10))
        self.assertEqual(True, main.task_7(29, 30, 6))
        self.assertEqual(False, main.task_7(20, 72, -1))
        self.assertEqual(False, main.task_7(10, 14, 69))
        self.assertEqual(True, main.task_7(45, 56, 88))
        self.assertEqual(False, main.task_7(33, 12, 16))
        self.assertEqual(True, main.task_7(87, 66, 99))
        self.assertEqual(True, main.task_7(66, 33, 81))
        self.assertEqual(False, main.task_7(43, 47, 0))
        self.assertEqual(True, main.task_7(56, 76, 82))
        self.assertEqual(True, main.task_7(95, 34, 88))
        self.assertEqual(False, main.task_7(17, 59, 20))
        self.assertEqual(True, main.task_7(25, 63, 40))
        self.assertEqual(False, main.task_7(8, 38, -1))
        self.assertEqual(False, main.task_7(20, -3, 92))
        self.assertEqual(False, main.task_7(-3, 63, 19))
        self.assertEqual(False, main.task_7(76, 48, 3))
        self.assertEqual(False, main.task_7(17, -4, 26))
        self.assertEqual(False, main.task_7(95, 27, 39))
        self.assertEqual(True, main.task_7(76, 55, 59))
        self.assertEqual(False, main.task_7(47, 92, 17))
        self.assertEqual(False, main.task_7(-2, 71, 6))
        self.assertEqual(False, main.task_7(4, -2, 14))
        self.assertEqual(False, main.task_7(55, 9, 17))
        self.assertEqual(False, main.task_7(84, 69, -5))
        self.assertEqual(True, main.task_7(90, 97, 74))
        self.assertEqual(True, main.task_7(92, 81, 43))
        self.assertEqual(False, main.task_7(23, 41, 97))
        self.assertEqual(False, main.task_7(35, 7, 47))
        self.assertEqual(False, main.task_7(8, 38, 81))
        self.assertEqual(True, main.task_7(37, 73, 37))
        self.assertEqual(False, main.task_7(31, 40, 2))
        self.assertEqual(False, main.task_7(22, 98, 14))
        self.assertEqual(False, main.task_7(5, 29, 77))
        self.assertEqual(False, main.task_7(26, 98, 39))
        self.assertEqual(False, main.task_7(11, 91, 74))
        self.assertEqual(True, main.task_7(85, 90, 69))
        self.assertEqual(False, main.task_7(37, 27, 89))
        self.assertEqual(False, main.task_7(81, 18, 2))
        self.assertEqual(False, main.task_7(29, 16, 98))
        self.assertEqual(False, main.task_7(84, 63, 5))
        self.assertEqual(False, main.task_7(56, 97, 5))
        self.assertEqual(False, main.task_7(6, 92, 2))
        self.assertEqual(False, main.task_7(21, 36, 92))