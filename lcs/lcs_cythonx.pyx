import time
import sys
import numpy as np
from libc.stdint cimport int32_t
from cython.view cimport array as cvarray
cpdef int lcs(int[:] a, int[:] b):
    cdef int n = len(a)
    cdef int m = len(b)
    cdef int[:,:] dp = cvarray(shape=(n+1, m+1), itemsize=sizeof(int), format="i")
    cdef int i, j
    for i in range(n+1):
        for j in range(m+1):
            dp[i,j] = 0
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i+1, j+1] = dp[i,j] + 1
            else:
                dp[i+1, j+1] = max(dp[i, j+1], dp[i+1,j])
    return dp[n,m]

def run_lcs(n: int):
    rng = np.random.default_rng(1234567)
    a = rng.integers(0, 100, n, dtype=np.int32)
    b = rng.integers(0, 100, n, dtype=np.int32)
    tic = time.perf_counter()
    lcs(a,b)
    toc = time.perf_counter()
    print(f"Cython pyx,{n},{toc - tic:0.4f}")

def main(n: int):
    run_lcs(n)

if __name__ == "__main__":
    n = 40_000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    main(n)
