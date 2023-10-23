import unittest
import main


class TestModule3(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual("PRIME", main.task_1(313))
        self.assertEqual("1", main.task_1(1))
        self.assertEqual("ERROR", main.task_1(0))
        self.assertEqual("ERROR", main.task_1(-311))
        self.assertEqual("ERROR", main.task_1(-22))
        self.assertEqual("COMPOSITE", main.task_1(1595))
        self.assertEqual("COMPOSITE", main.task_1(72))
        self.assertEqual("COMPOSITE", main.task_1(1843))
        self.assertEqual("COMPOSITE", main.task_1(2678))
        self.assertEqual("COMPOSITE", main.task_1(3848))
        self.assertEqual("COMPOSITE", main.task_1(3675))
        self.assertEqual("COMPOSITE", main.task_1(3337))
        self.assertEqual("COMPOSITE", main.task_1(1809))
        self.assertEqual("COMPOSITE", main.task_1(3091))
        self.assertEqual("PRIME", main.task_1(2437))
        self.assertEqual("COMPOSITE", main.task_1(813))
        self.assertEqual("COMPOSITE", main.task_1(1684))
        self.assertEqual("COMPOSITE", main.task_1(2474))
        self.assertEqual("COMPOSITE", main.task_1(2750))
        self.assertEqual("PRIME", main.task_1(2281))
        self.assertEqual("COMPOSITE", main.task_1(3651))
        self.assertEqual("COMPOSITE", main.task_1(2575))
        self.assertEqual("COMPOSITE", main.task_1(3818))
        self.assertEqual("PRIME", main.task_1(757))
        self.assertEqual("COMPOSITE", main.task_1(2112))
        self.assertEqual("COMPOSITE", main.task_1(955))
        self.assertEqual("COMPOSITE", main.task_1(1056))
        self.assertEqual("COMPOSITE", main.task_1(2230))
        self.assertEqual("COMPOSITE", main.task_1(3969))
        self.assertEqual("COMPOSITE", main.task_1(3972))
        self.assertEqual("COMPOSITE", main.task_1(3378))
        self.assertEqual("COMPOSITE", main.task_1(1930))
        self.assertEqual("PRIME", main.task_1(1367))
        self.assertEqual("COMPOSITE", main.task_1(3948))

    def test_task_2(self):
        self.assertEqual(198, main.task_2(49302, 152856))
        self.assertEqual(23, main.task_2(40917, 34339))
        self.assertEqual(49, main.task_2(77322, 58555))
        self.assertEqual(57, main.task_2(67260, 74157))
        self.assertEqual(100, main.task_2(59100, 19100))
        self.assertEqual(22, main.task_2(33770, 43626))
        self.assertEqual(35, main.task_2(57155, 38955))
        self.assertEqual(188, main.task_2(168260, 25004))
        self.assertEqual(148, main.task_2(140156, 135420))
        self.assertEqual(7, main.task_2(6433, 6993))
        self.assertEqual(75, main.task_2(51225, 33600))
        self.assertEqual(15, main.task_2(11520, 28245))
        self.assertEqual(90, main.task_2(72450, 89820))
        self.assertEqual(198, main.task_2(90882, 125532))
        self.assertEqual(208, main.task_2(44928, 30160))
        self.assertEqual(574, main.task_2(39606, 163016))
        self.assertEqual(96, main.task_2(24480, 5952))
        self.assertEqual(42, main.task_2(52626, 28896))
        self.assertEqual(62, main.task_2(75578, 62806))
        self.assertEqual(244, main.task_2(45628, 112972))
        self.assertEqual(57, main.task_2(89604, 34143))
        self.assertEqual(74, main.task_2(27602, 94720))
        self.assertEqual(24, main.task_2(36168, 11472))
        self.assertEqual(75, main.task_2(128550, 40275))
        self.assertEqual(66, main.task_2(22638, 15576))
        self.assertEqual(176, main.task_2(163504, 88352))
        self.assertEqual(44, main.task_2(59312, 72468))
        self.assertEqual(43, main.task_2(32895, 65833))
        self.assertEqual(91, main.task_2(28665, 41041))
        self.assertEqual(65, main.task_2(57200, 103805))
        self.assertEqual(2, main.task_2(3046, 862))
        self.assertEqual(2, main.task_2(3044, 966))
        self.assertEqual(2, main.task_2(540, 1082))
        self.assertEqual(9, main.task_2(1836, 1395))
        self.assertEqual(1, main.task_2(1759, 720))

    def test_task_3(self):
        self.assertEqual([3.5], main.task_3(0, 12, -42))
        self.assertEqual([10.582575694955839, 1.4174243050441602], main.task_3(-1, 12, -15))
        self.assertEqual([3.5, 3.0], main.task_3(-2, 13, -21))
        self.assertEqual([-1.674772708486752, 1.074772708486752], main.task_3(5, 3, -9))
        self.assertEqual([-3.6203345213916034, 13.120334521391603], main.task_3(2, -19, -95))
        self.assertEqual([-0.8666666666666667], main.task_3(0, 15, 13))
        self.assertEqual([], main.task_3(5, -10, 86))
        self.assertEqual([], main.task_3(4, -9, 27))
        self.assertEqual([2.131043674065006, -5.6310436740650065], main.task_3(-2, -7, 24))
        self.assertEqual([4.309447398198282, -3.1094473981982818], main.task_3(-5, 6, 67))
        self.assertEqual([-4.523702512552136, 0.7737025125521364], main.task_3(4, 15, -14))
        self.assertEqual([-6.289197915623474, 11.289197915623474], main.task_3(1, -5, -71))
        self.assertEqual([-1.7362373841740268, -3.263762615825973], main.task_3(-3, -15, -17))
        self.assertEqual([], main.task_3(1, -5, 44))
        self.assertEqual([-4.772001872658765, 3.7720018726587656], main.task_3(3, 3, -54))
        self.assertEqual([-0.6937742251701451, -2.306225774829855], main.task_3(-5, -15, -8))
        self.assertEqual([9.848857801796104, -9.848857801796104], main.task_3(-1, 0, 97))
        self.assertEqual([], main.task_3(-2, -18, -48))
        self.assertEqual([8.214438992364412, -2.8811056590310797], main.task_3(-3, 16, 71))
        self.assertEqual([], main.task_3(4, 1, 12))
        self.assertEqual([-1.8788253360656313, 10.378825336065631], main.task_3(2, -17, -39))
        self.assertEqual([0.0, 2.6], main.task_3(5, -13, 0))
        self.assertEqual([], main.task_3(-2, 15, -52))
        self.assertEqual([], main.task_3(-5, -15, -36))
        self.assertEqual([], main.task_3(-5, 5, -100))
        self.assertEqual([], main.task_3(-3, 15, -28))
        self.assertEqual([3.1596460097781875, -12.659646009778188], main.task_3(-2, -19, 80))
        self.assertEqual([], main.task_3(5, 5, 69))
        self.assertEqual([-2.9313902456001077, 7.931390245600108], main.task_3(4, -20, -93))
        self.assertEqual([9.1041219597369, -0.6041219597368999], main.task_3(-2, 17, 11))
        # handwritten cases
        self.assertEqual([-2.0, -1.0], main.task_3(1, 3, 2))
        self.assertEqual([0.0], main.task_3(0, 3, 0))
        self.assertEqual([-3.0], main.task_3(1, 6, 9))

    def test_task_4(self):
        self.assertEqual([-128, 280, 115, -503, 410, 261, -373, -126],
                         main.task_4([-8, 13, 18, -18, -7], [16, -9, 7, 18]))
        self.assertEqual([-30, -34, -28, 22, -2, 8], main.task_4([-15, -17, -14, 11, -1, 4], [2]))
        self.assertEqual([52, -221, 257, 65, -204], main.task_4([-13, 13, 17], [-4, 13, -12]))
        self.assertEqual([-187, 337, -127, 6, 98, -616, 737, -64, -326, 140],
                         main.task_4([17, -9, -20, 14], [-11, 14, -13, 19, -11, -9, 10]))
        self.assertEqual([64, -168, 274, -565, 350, -353, 190, 296, 123, 153],
                         main.task_4([4, -9, 9, -17], [16, -6, 19, -17, -19, -12, -9]))
        self.assertEqual([80, 40, 144, 56, -144, -24, 16], main.task_4([10, 5, 18, 7, -18, -3, 2], [8]))
        self.assertEqual([204, -149, 120, -316, -3, -440, 286, -300, -102],
                         main.task_4([17, -11, -15, -12, 20, -18, -6], [12, -1, 17]))
        self.assertEqual([0, 204, 349, -59, -360, -221], main.task_4([0, -12, -17], [-17, -5, 12, 13]))
        self.assertEqual([0, 0, 160, -468, 396, 40, 432, -435, -11, 36, 255],
                         main.task_4([0, -8, 17, -3, -16, -17], [0, -20, 16, -8, 12, -15]))
        self.assertEqual([95, 227, -166, -33, 12], main.task_4([19, -4], [5, 13, -6, -3]))
        self.assertEqual([-304, -80, 272, 272], main.task_4([16], [-19, -5, 17, 17]))
        self.assertEqual([26, 14, 69, 55, -75, -19, 7, -140], main.task_4([2, 0, 7], [13, 7, -11, 3, 1, -20]))
        self.assertEqual([-56, -166, -197, -365, -333, -38], main.task_4([14, 17, 2], [-4, -7, -5, -19]))
        self.assertEqual([361, 380, 228, -114], main.task_4([-19], [-19, -20, -12, 6]))
        self.assertEqual([-247, -403, -39, 234, -78, -286, -169, -78],
                         main.task_4([13, 13], [-19, -12, 9, 9, -15, -7, -6]))
        self.assertEqual([-224, -290, 159, 743, -27, -901, -299, 685, 223, -620, -320],
                         main.task_4([-16, 1, 18, 19, -19, -16], [14, 19, 7, -8, 15, 20]))
        self.assertEqual([-80, 80, -360, 300], main.task_4([-20], [4, -4, 18, -15]))
        self.assertEqual([44, -154, 99, 33, 22, 55, -88], main.task_4([4, -14, 9, 3, 2, 5, -8], [11]))
        self.assertEqual([-15, -20], main.task_4([15, 20], [-1]))
        self.assertEqual([119, -255, 52, 96], main.task_4([7, -8], [17, -17, -12]))
