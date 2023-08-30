# will return number of func() calls for which func() == expected
def random_test(expected, times: int):
    def random_test_decorator(func):
        def _wrapper(*args, **kwargs):
            ctr = 0
            for _ in range(times):
                if func(*args, **kwargs) == expected:
                    ctr += 1
            return ctr

        return _wrapper

    return random_test_decorator
