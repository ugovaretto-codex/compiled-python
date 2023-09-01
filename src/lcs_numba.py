import sys
import time
import numpy as np
import numba

#longest common subsequence
@numba.njit
def lcs(a, b):
    dp = np.zeros((len(a)+1, len(b)+1), dtype=np.int32)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

def run_lcs(n: int):
    rng = np.random.default_rng(1234567)
    a = rng.integers(0, 100, n, dtype=np.int32)
    b = rng.integers(0, 100, n, dtype=np.int32)
    tic = time.perf_counter()
    lcs(a,b)
    toc = time.perf_counter()
    print(f"Numba,{n},{toc - tic:0.4f}")

def main(n: int):
    run_lcs(n)

if __name__ == "__main__":
    n = 40_000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    main(n)
