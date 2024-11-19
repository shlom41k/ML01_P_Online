import random

GLOBAL_CACHE = dict()


def cache_wrapper(func):
    def wrapped(*args, **kwargs):
        context = GLOBAL_CACHE.get(id(func))

        if context is not None and context[0] < 3:
            value = context[1]
            itt = context[0]

            GLOBAL_CACHE.update({id(func): [itt + 1, value]})
        else:
            print("Update context for " + func.__name__ + " (" + str(id(func)) + ")")
            GLOBAL_CACHE.update({id(func): [0, func(*args, **kwargs)]})

        return GLOBAL_CACHE.get(id(func))[1]

    return wrapped


@cache_wrapper
def func_for_test_0(a: int):
    return 2 ** a


@cache_wrapper
def func_for_test_1(a: int):
    return a * a * a


@cache_wrapper
def func_for_test_2(a: int):
    return (358 * a) % 10


if __name__ == "__main__":
    print("GLOBAL_CACHE: ", GLOBAL_CACHE)
    print("-" * 120)

    for i in range(10):
        r_0 = func_for_test_0(random.randint(0, 10))
        r_1 = func_for_test_1(random.randint(0, 10))
        r_2 = func_for_test_2(random.randint(0, 10))

        print()
        print("GLOBAL_CACHE: ", GLOBAL_CACHE)

        print()
        print("Results of functions: func_0 = " + str(r_0) + " func_1 = " + str(r_1) + " func_2 = " + str(r_2))
        print("-"*120)


"""
GLOBAL_CACHE:  {}
------------------------------------------------------------------------------------------------------------------------
Update context for func_for_test_0 (2286583420384)
Update context for func_for_test_1 (2286583420672)
Update context for func_for_test_2 (2286583420960)

GLOBAL_CACHE:  {2286583420384: [0, 1], 2286583420672: [0, 343], 2286583420960: [0, 4]}

Results of functions: func_0 = 1 func_1 = 343 func_2 = 4
------------------------------------------------------------------------------------------------------------------------

GLOBAL_CACHE:  {2286583420384: [1, 1], 2286583420672: [1, 343], 2286583420960: [1, 4]}

Results of functions: func_0 = 1 func_1 = 343 func_2 = 4
------------------------------------------------------------------------------------------------------------------------

GLOBAL_CACHE:  {2286583420384: [2, 1], 2286583420672: [2, 343], 2286583420960: [2, 4]}

Results of functions: func_0 = 1 func_1 = 343 func_2 = 4
------------------------------------------------------------------------------------------------------------------------

GLOBAL_CACHE:  {2286583420384: [3, 1], 2286583420672: [3, 343], 2286583420960: [3, 4]}

Results of functions: func_0 = 1 func_1 = 343 func_2 = 4
------------------------------------------------------------------------------------------------------------------------
Update context for func_for_test_0 (2286583420384)
Update context for func_for_test_1 (2286583420672)
Update context for func_for_test_2 (2286583420960)

GLOBAL_CACHE:  {2286583420384: [0, 512], 2286583420672: [0, 512], 2286583420960: [0, 6]}

Results of functions: func_0 = 512 func_1 = 512 func_2 = 6
------------------------------------------------------------------------------------------------------------------------

GLOBAL_CACHE:  {2286583420384: [1, 512], 2286583420672: [1, 512], 2286583420960: [1, 6]}

Results of functions: func_0 = 512 func_1 = 512 func_2 = 6
------------------------------------------------------------------------------------------------------------------------

GLOBAL_CACHE:  {2286583420384: [2, 512], 2286583420672: [2, 512], 2286583420960: [2, 6]}

Results of functions: func_0 = 512 func_1 = 512 func_2 = 6
------------------------------------------------------------------------------------------------------------------------

GLOBAL_CACHE:  {2286583420384: [3, 512], 2286583420672: [3, 512], 2286583420960: [3, 6]}

Results of functions: func_0 = 512 func_1 = 512 func_2 = 6
------------------------------------------------------------------------------------------------------------------------
Update context for func_for_test_0 (2286583420384)
Update context for func_for_test_1 (2286583420672)
Update context for func_for_test_2 (2286583420960)

GLOBAL_CACHE:  {2286583420384: [0, 2], 2286583420672: [0, 343], 2286583420960: [0, 8]}

Results of functions: func_0 = 2 func_1 = 343 func_2 = 8
------------------------------------------------------------------------------------------------------------------------

GLOBAL_CACHE:  {2286583420384: [1, 2], 2286583420672: [1, 343], 2286583420960: [1, 8]}

Results of functions: func_0 = 2 func_1 = 343 func_2 = 8
------------------------------------------------------------------------------------------------------------------------
"""