import numpy as np
import cython
import sys
import time

#longest common subsequence
@cython.locals(i=cython.int, j=cython.int, a=list[cython.int], b=list[cython.int])
@cython.boundscheck(False)
@cython.wraparound(False) 
def lcs(a: list[int], b: list[int]) -> int:
    m = len(a)
    n = len(b)
    dp = [[0] * (m+1) for _ in range (n+1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def run_lcs(n: int):
    rng = np.random.default_rng(1234567)
    a = rng.integers(0, 100, n, dtype=np.int32).tolist()
    b = rng.integers(0, 100, n, dtype=np.int32).tolist()
    tic = time.perf_counter()
    lcs(a,b)
    toc = time.perf_counter()
    print(f"Cython annotated,{n},{toc - tic:0.4f}")

def main(n: int):
    run_lcs(n)

if __name__ == "__main__":
    n = 40_000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    main(n)
