import sys
import time
import numpy as np
#longest common subsequence
def lcs(a: list[int], b: list[int]) -> int:
    dp = [[0] * (len(b)+1) for _ in range (len(a)+1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

def run_lcs(n: int, tag):
    rng = np.random.default_rng(1234567)
    a = rng.integers(0, 100, n, dtype=np.int32).tolist()
    b = rng.integers(0, 100, n, dtype=np.int32).tolist()
    tic = time.perf_counter()
    lcs(a,b)
    toc = time.perf_counter()
    print(f"{tag},{n},{toc - tic:0.4f}")

def main(n: int, tag: str):
    run_lcs(n, tag)

if __name__ == "__main__":
    n = 40_000
    tag = "CPython" 
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    if len(sys.argv) == 3:
        tag = sys.argv[2]
    main(n, tag)
