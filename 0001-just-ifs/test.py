import unittest
import main

class TestModule1(unittest.TestCase):
    def test_task_1(self):
        # first less/equal -> return min
        self.assertEqual(main.task_1(1, 2, 3), 1)
        self.assertEqual(main.task_1(5, 2, 3), 2)
        self.assertEqual(main.task_1(1, 20, -4), -4)
        self.assertEqual(main.task_1(-100, -2, -3), -100)
        # first greater -> return 2nd
        self.assertEqual(main.task_1(100, 2, 3), 2)
        self.assertEqual(main.task_1(13, -2000, 3), -2000)
        self.assertEqual(main.task_1(-12, -2, -13), -2)
        self.assertEqual(main.task_1(1000, 0, 300), 0)
        # random
        self.assertEqual(main.task_1(-235, -511, -402), -511)
        self.assertEqual(main.task_1(-438, -57, 729), -438)
        self.assertEqual(main.task_1(-257, -806, 1000), -806)
        self.assertEqual(main.task_1(-158, 372, 726), -158)
        self.assertEqual(main.task_1(-25, 236, -343), 236)
        self.assertEqual(main.task_1(-918, -141, -143), -918)
        self.assertEqual(main.task_1(311, -827, 950), -827)
        self.assertEqual(main.task_1(229, 552, 730), 229)
        self.assertEqual(main.task_1(489, -264, 157), -264)
        self.assertEqual(main.task_1(52, 80, 55), 52)

    def test_task_2(self):
        self.assertEqual(main.task_2(933, 84, -70), 84)
        self.assertEqual(main.task_2(-429, 508, -495), -495)
        self.assertEqual(main.task_2(-65, -678, -13), -678)
        self.assertEqual(main.task_2(112, 711, -243), -243)
        self.assertEqual(main.task_2(866, 823, -924), -924)
        self.assertEqual(main.task_2(-712, -972, -753), -972)
        self.assertEqual(main.task_2(-623, 192, -962), 192)
        self.assertEqual(main.task_2(-266, -568, -703), -266)
        self.assertEqual(main.task_2(-967, -149, -18), -18)
        self.assertEqual(main.task_2(-956, 542, 566), 566)
        self.assertEqual(main.task_2(-230, -705, 692), -705)
        self.assertEqual(main.task_2(-311, -957, 100), -957)
        self.assertEqual(main.task_2(98, 561, 717), 561)
        self.assertEqual(main.task_2(-579, -617, -364), -579)
        self.assertEqual(main.task_2(533, 268, 581), 581)
        self.assertEqual(main.task_2(708, -146, -539), 708)
        self.assertEqual(main.task_2(-328, -455, 98), 98)
        self.assertEqual(main.task_2(63, -64, -459), -459)
        self.assertEqual(main.task_2(131, -182, -846), -846)
        self.assertEqual(main.task_2(536, 157, -708), -708)

    def test_task_3(self):
        self.assertEqual(main.task_3(-89, 792, -371), 1163)
        self.assertEqual(main.task_3(-116, -623, -506), 507)
        self.assertEqual(main.task_3(299, -545, -938), 1237)
        self.assertEqual(main.task_3(56, 585, 254), 529)
        self.assertEqual(main.task_3(-399, 300, -281), 699)
        self.assertEqual(main.task_3(-388, 733, -866), 1437789)
        self.assertEqual(main.task_3(-287, -962, -210), 1051913)
        self.assertEqual(main.task_3(-227, -62, -472), 278157)
        self.assertEqual(main.task_3(231, 684, 996), 1513233)
        self.assertEqual(main.task_3(655, -386, -376), 719397)
        self.assertEqual(main.task_3(915, 166, 697), 749)
        self.assertEqual(main.task_3(-989, -579, 617), 1694051)
        self.assertEqual(main.task_3(-454, 909, -12), 1032541)
        self.assertEqual(main.task_3(-939, 124, 303), 1242)
        self.assertEqual(main.task_3(171, -721, 61), 552803)
        self.assertEqual(main.task_3(705, -854, -225), 1559)
        self.assertEqual(main.task_3(795, 676, -181), 976)
        self.assertEqual(main.task_3(-37, 35, 855), 733619)
        self.assertEqual(main.task_3(-144, -490, -983), 1227125)
        self.assertEqual(main.task_3(-291, -448, 318), 386509)

if __name__ == '__main__':
    unittest.main()