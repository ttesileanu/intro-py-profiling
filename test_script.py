import numpy as np

if __name__ == "__main__":
    n = 5000
    p = 3

    rng = np.random.default_rng(0)
    a = rng.normal(size=(n, n))
    b = rng.normal(size=n)

    ap = np.eye(n)
    for i in range(p):
        ap = np.dot(ap, a)

    x = np.linalg.solve(ap, b)
