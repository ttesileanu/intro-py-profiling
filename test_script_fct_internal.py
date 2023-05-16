import numpy as np
import cProfile


def setup(n):
    rng = np.random.default_rng(0)
    a = rng.normal(size=(n, n))
    b = rng.normal(size=n)

    return a, b


def mpower(a, p):
    ap = np.eye(len(a))
    for i in range(p):
        ap = ap @ a

    return ap


def solve(a, b):
    x = np.linalg.solve(a, b)
    return x


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()

    n = 5000
    p = 3

    a, b = setup(n)
    ap = mpower(a, p)
    solve(ap, b)

    pr.disable()
    pr.dump_stats("test_script_fct_internal.prof")
    pr.print_stats(sort="cumtime")
