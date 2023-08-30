import random

def rand_int_arr(min_size: int, max_size: int, min_val: int, max_val: int) -> list[int]:
    size = random.randint(min_size, max_size)
    res = []
    for i in range(size):
        res.append(random.randint(min_val, max_val))
    return res

def rand_str(min_len: int, max_len: int) -> str:
    s = ''
    length = random.randint(min_len, max_len)
    for i in range(length):
        if random.random() < 0.1:
            s += ' '
            continue
        upper = random.randint(0,1)
        if (upper == 1):
            s += chr(65 + random.randint(0, 25))
        else:
            s += chr(97 + random.randint(0, 25))
    return s

def rand_str_arr(min_size: int, max_size: int, min_len: int, max_len: int) -> list[str]:
    size = random.randint(min_size, max_size)
    res = []
    for i in range(size):
        res.append(rand_str(min_len, max_len))
    return res

