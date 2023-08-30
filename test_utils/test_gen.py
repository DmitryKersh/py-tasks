from solutions import *
from test_gen_utils import *

times = int(input("number of tests?"))
for i in range(times):
    n1 = random.randint(-100, 100)
    n2 = random.randint(-100, 100)
    n3 = random.randint(-100, 100)
    arr1 = rand_int_arr(1, 7, -20, 20)
    arr2 = rand_int_arr(1, 7, -20, 20)
    s = rand_str(50, 100)
    delims = rand_str_arr(2, 10, 1, 1)
    print("self.assertEqual({}, main.task_6({}, {}, {}))".format(module_1_task_6(n1, n2, n3), n1, n2, n3))

# cases = [0, 1000, 1_000_000, 2_000_009, 12_012_001, 500_000_000_312, 500_000_312_000, 500_132_000_000, 500_001_002_003, 123_456_789_012]
cases = [
    [10, 30, 20],
    [10, 31, 20],
    [10, 29, 20],
    [10, 30, 19],
    [10, 31, 21],
    [10, 30, 21],
]
print("# handwritten cases")
for n in cases:
    print("self.assertEqual({}, main.task_6({}, {}, {}))".format(module_1_task_6(n[0], n[1], n[2]), n[0], n[1], n[2]))
