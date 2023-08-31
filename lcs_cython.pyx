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

def run_lcs():
    rng = np.random.default_rng(12345)
    n = 30_000
    a = rng.integers(0, 100, n, dtype=np.int32)
    b = rng.integers(0, 100, n, dtype=np.int32)
    s = lcs(a,b)
    print(s)

def main():
    run_lcs()

if __name__ == "__main__":
    main()
