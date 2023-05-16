import numpy as np


@profile
def work():
    n = 5000
    p = 3

    rng = np.random.default_rng(0)
    a = rng.normal(size=(n, n))
    b = rng.normal(size=n)

    ap = np.eye(n)
    for i in range(p):
        ap = ap @ a

    x = np.linalg.solve(ap, b)


if __name__ == "__main__":
    work()
