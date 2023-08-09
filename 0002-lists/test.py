import unittest
import main

class TestModule2(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual([78],
                         main.task_1([78, -27, -71, 64, 31, -65, 31, -15, 27, -12, 20, -17, 94, 80, -27, 65, 54], 8))
        self.assertEqual([], main.task_1(
            [-24, -40, -71, -25, 4, 67, 5, 8, 77, 55, 6, 32, 46, 6, -61, -63, -77, 56, -80, -93, -44, -93, 82], 0))
        self.assertEqual([59, 49],
                         main.task_1([48, 25, -52, -17, -47, 36, 59, -73, 58, 49, 70, 75, -27, -26, -94, -50], 9))
        self.assertEqual([-1, 61, -21, 61], main.task_1(
            [-49, 46, -67, 33, -1, 61, -21, 61, -84, 98, -98, -78, -88, 66, -87, 35, 47, 36, -99, -56, -75, -28, 24],
            1))
        self.assertEqual([], main.task_1(
            [-71, -1, -18, -41, -60, 52, -68, -99, -95, 84, 25, -58, 83, -47, -33, -24, -3, 21, -77, 41, -66, 92, -44,
             -88], 0))
        self.assertEqual([], main.task_1(
            [56, -30, 52, -7, -34, 94, 34, 89, 51, -61, 25, 93, 3, 26, -70, 84, 8, 87, -70, 87, -77], 0))
        self.assertEqual([-42, 32],
                         main.task_1([-26, 56, -55, 43, -87, -15, 8, -42, -40, -15, 87, 46, 97, -98, 100, 32, -50], 2))
        self.assertEqual([-75], main.task_1([-34, -99, -33, 29, 76, 32, -75, 89, 73, 22, -87, 26, -90, -24], 5))
        self.assertEqual([20], main.task_1(
            [87, -83, 66, -25, 16, 34, 64, -87, 6, 48, 71, -19, -66, 78, 52, -40, -72, -10, -89, 56, 72, 20], 0))
        self.assertEqual([], main.task_1([11, -66, 73, -91, 61, -43, -60, -1, -36, 88, -66], 9))
        self.assertEqual([], main.task_1([-43, -53, 70, 71, -4, 53, -24, 68, -6, 55, -11], 7))
        self.assertEqual([81], main.task_1([-49, 81, -85, -98, -23, 67, 72, -15, -97, 63, -34], 1))
        self.assertEqual([92], main.task_1(
            [90, 89, 26, 3, -13, 83, 4, 6, -15, -54, 3, -63, 41, -96, 92, 21, 97, 83, 96, 68, -79], 2))
        self.assertEqual([], main.task_1([53, 80, 43, -71, 97, 34, -66, -43, -42, -49, 76, -26, 3, 29, -1, 68], 5))
        self.assertEqual([], main.task_1([28, -8, -59, 5, 84, -36, -20, -2, -75, -86], 10))
        self.assertEqual([86, 66, 46], main.task_1(
            [-53, 5, 37, -24, -12, -48, 34, -2, 86, 64, 66, 90, 95, -53, 32, -98, -21, 46, -34, 5, 73, -90, -79, -69],
            6))
        self.assertEqual([], main.task_1([64, 51, -82, 67, 11, -24, -39, 97, -57, 92, -54], 6))
        self.assertEqual([], main.task_1([66, -72, 99, 37, 82, 89, 33, -5, -87, 69, -24], 0))
        self.assertEqual([],
                         main.task_1([60, 100, 20, 82, -91, 47, 48, 78, -16, 33, -78, -33, -66, -42, -13, -75, -7, 34],
                                     -1))
        self.assertEqual([88], main.task_1(
            [-83, -13, 54, -59, 59, -85, 10, -62, 88, 0, 67, -20, -29, 40, -89, 22, 66, -92, 73, 45], 8))
        self.assertEqual([77, -77], main.task_1(
            [6, -96, 41, 14, 80, 39, -99, -70, 68, -70, -34, -49, 85, 18, 77, 90, 22, -53, 48, -77, 63], 7))
        self.assertEqual([], main.task_1(
            [31, -98, -45, -13, -35, 6, 23, 70, 19, -77, 15, 4, -69, 26, -37, 73, -66, 73, -37, -13, 15, 72, -54, 74,
             23], 10))
        self.assertEqual([69, -89], main.task_1([43, -55, 69, 53, -22, 37, 50, -89, 83, 13, 7, -72, -67], 9))
        self.assertEqual([], main.task_1(
            [0, 10, -31, 14, 12, -4, 90, 50, 32, -49, 52, -17, 3, 95, -43, -83, 68, 53, -58, 61, -5, -70, -20, 53], 6))
        self.assertEqual([-57, 87], main.task_1([-94, -79, -4, -57, 60, 41, -64, -72, 55, -19, 87], 7))
        self.assertEqual([], main.task_1([-61, -13, -94, -11, -23, -81, -83, -62, 11, 96, -48], 7))
        self.assertEqual([14, -4, -74, 44], main.task_1([14, 89, -4, -56, -74, -40, 44, -69, -53, -58, -7, -2], 4))
        self.assertEqual([], main.task_1([84, 69, 4, -77, 77, -13, -63, -71, -67, -14], 8))
        self.assertEqual([], main.task_1([-17, -53, 24, -79, 23, -83, 7, 55, 84, 0, -54, 62], 1))
        self.assertEqual([24], main.task_1([-25, -52, 15, -33, 39, 7, -75, -89, 16, -26, -100, 58, -60, 24], 4))

    def test_task_2(self):
        self.assertEqual([67, 44, -22, -31, 18, -99], main.task_2(
            [17, 13, 38, -76, -59, -41, -84, -52, -11, -73, 31, 36, 67, 44, -22, -31, 18, -99]))
        self.assertEqual([99, -6, -54, -83], main.task_2(
            [59, 92, -2, -77, -12, 80, 99, -6, -54, -83, -83, -21, 52, 41, -69, 36, 64, 77, 88, 9, -56]))
        self.assertEqual([-74, -56, -5, -50, 63, 18, 60, -58, 49, 60, 89],
                         main.task_2([-10, -74, -56, -5, -50, 63, 18, 60, -58, 49, 60, 89, 47, -68]))
        self.assertEqual([-97, 83, 4, 94], main.task_2(
            [-23, -64, -24, -82, -1, -2, 10, -66, -41, 5, 16, -64, -97, 83, 4, 94, -15, -97, 56, -4, 16]))
        self.assertEqual([56, -57, -89],
                         main.task_2([-62, -4, 33, 32, -57, -21, -78, -9, 20, -5, -21, 56, -57, -89, 45]))
        self.assertEqual([78, 71, -1, -89, 59, -96], main.task_2(
            [-51, 8, 71, -35, 51, 10, 12, 7, -26, 53, -66, 21, 10, -9, -29, 68, 60, 78, 71, -1, -89, 59, -96, 14]))
        self.assertEqual([-91, -38, 22, 100], main.task_2(
            [-19, 72, -52, -91, -38, 22, 100, 42, -59, -18, -23, -4, 69, 97, -34, -60, -53, 50, 97]))
        self.assertEqual([95, -93, -22, -71, 8, 75, -22, 50, -45, -21, -13, 55, 50, -97], main.task_2(
            [9, -95, -14, 78, -64, 16, -23, 95, -93, -22, -71, 8, 75, -22, 50, -45, -21, -13, 55, 50, -97, 53]))
        self.assertEqual([95, -36, -5, 6, 71, 84, -88], main.task_2(
            [-40, 61, -35, 95, -36, -5, 6, 71, 84, -88, 51, 20, 68, 94, 56, -16, 48, 92, 16, 53, -37, -50]))
        self.assertEqual([90, 71, 64, -24, -14, 78, -28, -36, -8, -8, 40, 49, -60],
                         main.task_2([90, 71, 64, -24, -14, 78, -28, -36, -8, -8, 40, 49, -60, 52, -56, -15, 45]))
        self.assertEqual([-82, -79, 89], main.task_2([-31, -80, -38, -82, -79, 89, -53, -32, -43, -17, -48]))
        self.assertEqual([-100, -59, -85, -98, 59, -24, 96, -39, 18, -41, 79, 97], main.task_2(
            [85, 79, -51, 76, 86, -98, 36, -83, 51, -47, -100, -59, -85, -98, 59, -24, 96, -39, 18, -41, 79, 97, -95]))
        self.assertEqual([-91, -23, -27, 39, -60, -17, -25, -34, 28, 84, 82, 39, -64, 93], main.task_2(
            [-15, -13, -81, -1, -71, 86, -29, 89, 36, -83, -91, -23, -27, 39, -60, -17, -25, -34, 28, 84, 82, 39, -64,
             93]))
        self.assertEqual([-100, 68, -21, -33, -96, -84, -52, -20, 67, 33, 39, 85, 87],
                         main.task_2([-100, 68, -21, -33, -96, -84, -52, -20, 67, 33, 39, 85, 87, 27, -12, -31, 80]))
        self.assertEqual([-69, -65, 41], main.task_2([-1, 10, -69, -65, 41, -18, 5, 2, -65, -18, -51, -51, -28, -56]))
        self.assertEqual([81, -46, -45, 7, 62, 5, 56, -11, -81, -8, -35, -2, -37, 78, -100], main.task_2(
            [-79, -10, 57, 81, -46, -45, 7, 62, 5, 56, -11, -81, -8, -35, -2, -37, 78, -100, -56, -60, -25, -74, -5,
             28]))
        self.assertEqual([-92, -65, 52, -72, -82, 97], main.task_2(
            [24, 19, -70, 57, -70, -92, -65, 52, -72, -82, 97, 61, 44, 20, 76, 21, -3, 8, -65, 51, 64, -16]))
        self.assertEqual([-100, 13, -63, -61, -28, 81],
                         main.task_2([-83, 59, -100, 13, -63, -61, -28, 81, -5, 77, -48, -17]))
        self.assertEqual([-99, 37, 99],
                         main.task_2([-17, -34, -99, 37, 99, 69, 48, 97, 0, -84, -84, -42, 91, 44, 3, -22]))
        self.assertEqual([-92, -25, 100], main.task_2(
            [8, -4, -60, 73, -8, -92, -25, 100, -30, 2, -34, 29, 99, -48, 42, 74, 42, 95, -2, -89, -24, 65, 26, -74]))
        self.assertEqual([-96, 1, -44, 46, 95],
                         main.task_2([17, 28, 71, -64, -39, 63, 77, -15, 45, 18, -96, 1, -44, 46, 95, -67, -38]))
        self.assertEqual([85, -99], main.task_2(
            [-40, -69, -28, 2, 5, -87, -59, 85, -99, -69, 33, -11, -45, 4, -27, -93, -81, -87, 47, -11, -89]))
        self.assertEqual([-90, -3, -71, -87, 87, -62, 94],
                         main.task_2([-90, -3, -71, -87, 87, -62, 94, -77, 7, 23, -15]))
        self.assertEqual([94, -1, -54, -58, -64, -44, -54, 3, 62, 91, 25, -55, 10, -39, -80, -100], main.task_2(
            [-67, 39, -22, -9, 94, -1, -54, -58, -64, -44, -54, 3, 62, 91, 25, -55, 10, -39, -80, -100, -29, -60, 2, 2,
             48]))
        self.assertEqual([-96, 96, 97], main.task_2([-96, 96, 97, -22, -61, 63, 45, -81, -63, -12]))
        self.assertEqual([74, -15, -59, -35, -9, -67, 45, 60, -81], main.task_2(
            [6, 35, 3, 3, 21, -33, 45, 9, 34, -25, -7, 74, -15, -59, -35, -9, -67, 45, 60, -81, 29]))
        self.assertEqual([84, 68, 63, -95], main.task_2(
            [-7, -68, 70, -66, 4, -19, 14, 73, -17, -82, 84, 68, 63, -95, 71, -31, -25, -36, -15]))
        self.assertEqual([-72, -40, 32, -43, 63, 86],
                         main.task_2([32, -65, -3, -34, 17, -72, -40, 32, -43, 63, 86, -63, 3]))
        self.assertEqual([80, 12, -6, 24, -63, -39, -39, -75, -3, -40, -29, -99], main.task_2(
            [50, 80, 12, -6, 24, -63, -39, -39, -75, -3, -40, -29, -99, -85, -8, -1, -43, -36, 51, -40, 59, 80, 49,
             56]))
        self.assertEqual([97, 8, -21, -52, 15, 69, 23, 89, 2, 6, 36, -45, -96], main.task_2(
            [-8, -88, -77, -88, -42, 97, 8, -21, -52, 15, 69, 23, 89, 2, 6, 36, -45, -96, 57, -8, 90, -27, -79, -57]))

    def test_task3(self):
        self.assertEqual([88, 81],
                         main.task_3([1, 0, 62, 51, 88, -13, 23, 32, 28, 60, 6, -17, 28, 81, -26, 30, -34, 54]))
        self.assertEqual([77, 52], main.task_3([-46, 35, 5, 17, 46, 77, 17, 1, -72, 52]))
        self.assertEqual([95, 92], main.task_3(
            [73, -93, 61, 8, 9, 15, -36, 42, -44, 87, 92, -93, 95, -19, -92, -12, -48, 20, 51, -41]))
        self.assertEqual([93, 87], main.task_3([31, 85, 29, 93, 76, -16, -20, -35, 56, -85, -7, -13, 87, 63, -98, -33]))
        self.assertEqual([88, 79], main.task_3([-5, 88, 38, -75, 79, 42, 26, -40, -89, 47, 69, 70, -82]))
        self.assertEqual([95, 87], main.task_3(
            [-29, 87, -61, -36, -66, -46, -57, -31, 37, -58, -39, 82, -7, 95, 63, -70, -3, -7, 79, 38, -1, 13, -92, 54,
             -61]))
        self.assertEqual([98, 94],
                         main.task_3([2, -48, -39, -25, -79, -60, 84, -87, 74, 94, 32, -11, -17, 98, 64, 33, -78, 33]))
        self.assertEqual([93, 91], main.task_3([-67, -35, 17, 42, -65, 93, 76, 79, 81, 39, -20, -41, 77, 91, 38]))
        self.assertEqual([99, 81], main.task_3([-10, -7, 10, -39, 80, 42, -7, 75, 81, -91, 71, 11, 45, -46, 99, -24]))
        self.assertEqual([96, 92], main.task_3(
            [62, 90, 62, -51, -6, 54, 30, 96, 48, 70, -43, 58, 41, -7, 19, -31, 36, 80, 39, 92, -28, -62, 74, 52]))
        self.assertEqual([99, 98], main.task_3([-7, 83, -63, 62, 64, 39, 23, 84, 98, 85, 99, -34, -87, 16]))
        self.assertEqual([93, 83], main.task_3([83, 51, 47, 50, 33, -71, 74, -97, 72, 21, -9, 46, 93, -14, 15]))
        self.assertEqual([85, -1], main.task_3([-71, -7, -1, -87, -67, -30, -90, -13, 85, -60, -93]))
        self.assertEqual([100, 96], main.task_3(
            [-45, 39, 74, -70, -56, 12, -11, 45, -19, -28, -44, -8, -29, 100, 15, 96, -73, -24, -17, 62, 41, 61, -56,
             54]))
        self.assertEqual([99, 83], main.task_3([-36, 8, 80, -34, -68, -28, -84, -93, 19, 99, 38, 62, 83, 72, -46, 4]))
        self.assertEqual([100, 100], main.task_3(
            [-93, 32, -88, -21, 15, 65, -60, -36, -20, -65, -17, -6, -18, -53, 100, -32, -87, -64, 31, -48, 16, 100,
             46]))
        self.assertEqual([99, 92], main.task_3(
            [9, 79, -36, -69, 92, -95, 11, -66, 7, 91, -18, -63, -97, -10, -34, 63, 99, 60, -49, -72, -64, -54]))
        self.assertEqual([88, 86], main.task_3([-66, 28, -30, 88, -3, 86, -84, 24, -94, -42, -28, 41, 81, 83, -82, -7]))
        self.assertEqual([89, 87], main.task_3(
            [56, 84, 89, -21, 16, 20, -96, 61, 16, 69, 32, -2, 82, 32, -45, -63, -5, -94, -88, 87, -22]))
        self.assertEqual([97, 88], main.task_3(
            [-15, -26, -65, 24, -98, 88, 51, -38, -44, 20, -27, 12, -42, 97, 21, 72, -98, 58, 88, -82]))
        self.assertEqual([65, 63], main.task_3([-4, 35, -79, 18, 10, -93, -27, -95, 63, 8, 34, 56, -100, 65, -32]))
        self.assertEqual([94, 88], main.task_3(
            [-31, -26, -94, -30, 79, -76, -60, 94, -93, 88, -75, -28, 35, -41, 22, 55, -64, -46, -4]))
        self.assertEqual([71, 68], main.task_3([-41, 68, -3, -53, 5, -10, -86, 37, -22, 71, -25, 33, 50, -40, -76]))
        self.assertEqual([67, 44], main.task_3([67, 18, -92, 40, -50, -81, 44, -11, -3, -2, -94, -37]))
        self.assertEqual([95, 92], main.task_3([95, -25, -4, 80, 31, 84, 41, -42, 70, -28, 92, 40, -29]))
        self.assertEqual([96, 94], main.task_3(
            [77, 14, -75, -1, 52, 73, 72, -84, -81, 94, 15, -99, -70, -98, 59, -55, -26, 96, -87]))
        self.assertEqual([95, 50], main.task_3([95, -22, -34, -53, -72, 49, 49, -77, 50, 42, -6]))
        self.assertEqual([96, 90], main.task_3(
            [-47, -6, 34, -98, 69, 40, -84, -26, 46, -37, 96, -17, 5, 6, 90, -13, -54, 8, -71, 23, 40, -53]))
        self.assertEqual([95, 78], main.task_3(
            [-86, 37, -37, -74, -27, 75, -88, -51, 19, -17, -41, -56, 95, 72, 22, 78, -47, -88, -100, -82, 20, -81, -63,
             -23]))
        self.assertEqual([93, 78], main.task_3(
            [27, 78, -65, -52, -94, -64, 3, -46, -86, 29, 93, -50, 16, -53, -22, -70, -2, 0, -15, 7, -41]))

    def test_task_4(self):
        self.assertEqual([-3, -3, -10, 19, -13, 14],
                         main.task_4([-3, -6, 4, -16, -3, 11, -10, 5, 19, -17, -13, 5, -20, -19, 14],
                                     [3, -7, -2, -8, 3, -4, -2, 6, -5, 17, 7, 7, -12, -3, -10, -13, 9, 19, 20, -5, 14,
                                      -12, -13, 19]))
        self.assertEqual([7, 9, 9, -14],
                         main.task_4([0, 3, 7, 0, -1, -17, -7, 19, 9, 18, -16, 9, -15, -6, -14, 5, 15, 8],
                                     [4, -8, 9, 14, -19, -2, -12, 13, -8, -10, -20, 17, 7, -8, 14, 6, -14, -9, -10,
                                      -14]))
        self.assertEqual([-2, -3, -14, -2, -14], main.task_4(
            [2, -2, 18, 16, -13, 7, -3, 4, 9, -6, -13, 6, -20, 0, 17, -14, -7, -2, -14, -5, 11],
            [-3, -12, -14, -10, -3, -2, 3, 13, 3, -4]))
        self.assertEqual([-20, -4, 12, -5, 20, 13, -20, -18, -19, 20, 9], main.task_4(
            [-11, 0, -20, 10, 18, -16, -16, -4, 3, 18, -3, 1, 12, 15, -17, -5, 20, 13, -20, -18, -19, 20, 9],
            [-10, -6, -20, 16, 17, -4, 13, -18, -13, -5, -15, 12, -7, -10, 20, -20, -12, -19, 20, 9]))
        self.assertEqual([-17, 13, 3, -18, 6, 0, -18],
                         main.task_4([-14, -16, 5, -17, 13, 18, -10, 3, 9, -18, 19, 6, 0, -18],
                                     [11, -13, 6, 20, -1, 3, -18, 0, 13, 1, 16, -8, 20, 10, -17, 11, -9, 7]))
        self.assertEqual([-9, -6, 17, 16, 16],
                         main.task_4([-18, -1, -17, -2, -2, 20, -9, -6, 9, 6, 17, -17, 7, 15, 16, 0, 16, -15],
                                     [-6, -9, 16, 5, -11, -19, -11, 10, -20, 17, 8, -19, 3, -8, -12, -20, 12, -3]))
        self.assertEqual([-9, 7, -17, -14, -9, -10, -12],
                         main.task_4([-13, -15, -1, -9, 7, -17, 19, -14, -9, 6, 13, 8, -1, -18, 19, -10, -12],
                                     [-19, -16, -6, -9, 10, -16, -14, -8, -17, -10, 15, 7, 11, -20, 2, -12, 10]))
        self.assertEqual([-11, -13, 9], main.task_4([-7, 3, 8, -18, -11, 2, -13, -5, -2, -8, 9, 11, 2],
                                                    [10, -19, -20, -16, 14, 12, -1, -1, -13, -11, 6, 9, -14, 20]))
        self.assertEqual([20, -18, -12, 13, 6, 15, 6, 18, -8], main.task_4(
            [20, -18, 8, -12, -15, 5, -15, 13, -6, 6, 15, -16, 11, 4, -4, 8, -6, 6, 18, -8, 7, -7, 11],
            [2, -3, 6, 20, -2, -8, 9, 18, 18, 15, -20, 16, -5, 16, -20, 2, 13, 1, -12, -14, -18, -10, 10]))
        self.assertEqual([-15, -12, 0, 20, -12, 0],
                         main.task_4([5, -15, -12, 7, 0, -5, -1, 9, 15, 14, 20, 9, 10, -1, -12, 0, -4],
                                     [-17, -3, 4, 0, -13, 16, 3, -10, -15, 4, 20, -18, 8, 6, 20, 4, -18, -16, -14, -8,
                                      0, 4, -3, -12]))
        self.assertEqual([12, -6, 17, 14], main.task_4([20, 3, 1, 12, -5, -6, -20, 13, -10, 17, 14, 13],
                                                       [18, 5, -1, 17, -13, 16, 6, 14, -13, 0, -6, 10, 12, -6, 4]))
        self.assertEqual([15, 15, -19],
                         main.task_4([-4, 14, 1, 1, 15, 18, -5, -10, 7, -20, 15, 1, -14, -19, 5, 7, -14, 20],
                                     [15, -16, -3, -17, -9, -19, -8, 8, 8, -9, -15, 0, -12, 10, -7, -2]))
        self.assertEqual([16, 6, -5, -5, 14, 15, 17, -5],
                         main.task_4([7, 11, -8, 16, 6, -5, -19, -5, 14, 15, -14, 17, -5, -16],
                                     [4, -20, -6, 5, 16, 8, 6, 9, 17, 14, -13, 15, -11, -18, 13, 9, 15, -6, 10, -5]))
        self.assertEqual([-15, 20, -8, 12, 7, -7, -13, -17],
                         main.task_4([-19, -15, 20, 8, -8, -5, 12, 7, 14, -7, 1, 18, -13, -17],
                                     [20, 13, 19, -18, 0, 6, -11, -8, -15, 17, -13, -2, -3, 19, 3, 12, -7, 10, -4, 7,
                                      -7, -17, 12, -6, -10]))
        self.assertEqual([4, -8, 5, -7, -19, -9, -8, -17], main.task_4(
            [0, -16, 19, 13, -12, 4, -8, 5, -7, -19, 13, 10, -13, 17, -18, 6, -9, -10, 20, -8, -17, 12, 17, -15, -2],
            [-17, -20, -4, 9, -9, 7, 11, 5, -19, 9, -3, -14, -8, 11, -7, 8, 4]))
        self.assertEqual([1, 7, -9, 9, -9, -5, 7, 2, 7],
                         main.task_4([1, -1, 3, 8, 7, 20, 17, -14, -9, 9, -9, -5, 7, -16, 2, 7],
                                     [1, 7, -10, 9, 6, -8, -5, 2, -15, 18, 16, -9]))
        self.assertEqual([-7, 0, -4, 8, 18],
                         main.task_4([-7, -11, 13, -6, 19, 0, 3, 19, -4, -12, -12, 6, 8, -6, -3, 13, 18, 11],
                                     [-4, -7, -18, -18, -20, 18, 2, -16, 0, -5, 5, 17, 8, 7, -7, 5, 16, -10, 1, 8, -19,
                                      15, 7, -4]))
        self.assertEqual([17, 15], main.task_4([16, -11, -4, -6, -4, -18, 14, 17, 8, 18, -1, -7, 2, 15, -4],
                                               [17, 11, 13, 19, 13, 6, -2, -16, 11, 1, 15, -13]))
        self.assertEqual([16, 20, 15, 8, 3, -5, 8, 15, 8, -11, -15, 5, -15], main.task_4(
            [16, 20, 15, -6, 13, -13, -13, 8, 19, 3, -5, 0, 11, 9, 9, 8, -12, 15, 8, -11, -15, 5, 13, -15],
            [-15, 3, 15, 5, -9, 20, -10, -14, 3, -17, 8, -8, 10, -7, -4, -3, -5, -1, 2, -18, 14, 16, -17, 12, -11]))
        self.assertEqual([-1, 19, -13, -1, 15, 12, -5], main.task_4(
            [6, -1, 9, 19, -13, 10, -4, 0, -10, -14, 5, -1, 0, -11, 15, 12, -4, -10, -5, 4, 18, -19, 20, -17],
            [19, 15, 12, 15, 2, -2, -1, -12, 16, 13, 2, 8, 16, -9, -13, 17, -9, -5, 12, -6, -5, -18, -3]))
        self.assertEqual([12, 11, 6, 6, 15, 18, 11],
                         main.task_4([-9, 12, -20, 1, 1, -17, -15, 9, 11, 3, 2, 6, -15, 6, -20, -9, 15, 18, 11, 20, 7],
                                     [18, 6, 12, -12, -10, -18, -6, -2, -11, 19, 10, 18, 15, -2, 17, 19, 14, 13, 4, -1,
                                      11, 5, -14, 8, -14]))
        self.assertEqual([19, -13, 16, -10], main.task_4([6, 8, 19, -12, 13, -13, 11, 16, 8, -10, -2, -2],
                                                         [2, -13, 9, 3, 14, -3, -5, 9, 17, 16, 3, 19, 2, 9, -13, 1, 9,
                                                          10, 20, -10, 5]))
        self.assertEqual([-1, -4, -18, -1, -15],
                         main.task_4([13, -2, 20, 8, -1, -4, -19, -18, -20, -2, 17, 11, 20, 13, -1, -15, 2, 3],
                                     [-18, -4, 9, 16, 6, -1, 12, -17, -15, -10, -6, 9]))
        self.assertEqual([2, 8, -1, 8, 15, -1, -19],
                         main.task_4([20, 3, 3, -6, 16, 2, 8, -1, 8, -17, -15, 15, -10, 10, -8, -1, 20, -19],
                                     [-19, -1, -18, -2, -1, 1, -16, 18, 6, 13, -18, -18, 0, 11, -7, 12, 15, -16, 2, 8,
                                      15]))
        self.assertEqual([19, 20, 12, 12, -6, 11, -2, 4], main.task_4(
            [7, 1, -10, -13, -14, 19, 5, -7, 20, 6, -19, -12, 12, 12, 0, -6, -3, 11, -2, 4, -3],
            [12, 17, -2, 17, -2, -6, 19, -8, 16, 4, 11, -5, 13, 20, -18]))
        self.assertEqual([-15, 1, -18, -15, 15, -5], main.task_4(
            [0, 16, 20, 0, -15, 16, 1, 4, -18, 11, -15, 4, -14, 12, 19, 15, -5, 13, -11, -14, 13, 4],
            [1, 7, -18, -15, 15, -5, -9, -20, -20, -16]))
        self.assertEqual([-16, -3, -16, 16, 7],
                         main.task_4([14, 19, 1, 18, -7, -16, -3, -4, -2, -5, 3, 6, -16, -20, 16, 7, 0, 0, 15, 11],
                                     [20, -1, 9, 7, -10, -16, -3, -1, 20, 20, -3, 7, 16, 5, -9]))
        self.assertEqual([-2, 12, 3, 17, -17, 12, -13, -8],
                         main.task_4([-20, -16, -2, 16, -4, 12, 3, 17, -17, -19, 12, -13, 19, -4, -8],
                                     [17, -8, -15, 12, 12, -2, -13, 15, -18, -7, -17, 3, -2, -13, -2, 5]))
        self.assertEqual([4, -4, -19, -14, -18, -16],
                         main.task_4([-3, 13, 10, 4, -4, -19, -6, -14, -10, 5, 9, -8, -18, -16],
                                     [-11, -17, -14, -16, -5, -19, 3, -5, -18, 15, 4, 19, 3, -14, -5, 20, 11, -11, -4,
                                      1, -5, -2, -17, -4]))
        self.assertEqual([15, 20, 5, -1, 9, -7, -9, 17, 15],
                         main.task_4([-5, -5, 1, 2, 16, 15, 14, 20, 5, -1, -3, -3, 4, 9, -20, 4, -7, -9, 17, 2, 15, 12],
                                     [-9, 9, 20, 11, -13, -7, 5, 13, -9, 15, 11, -16, -15, 3, -1, -6, -10, -18, -1, 17,
                                      -14, -10, 6, -10, -18]))
