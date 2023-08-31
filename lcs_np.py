import numpy as np
import numpy.typing as npt

IntArray = npt.NDArray[np.int32]

#longest common subsequence
def lcs(a: IntArray, b: IntArray) -> np.int32:
    #dp = [[0] * (len(b)+1) for _ in range (len(a)+1)]
    dp : IntArray = np.zeros((len(a)+1, len(b)+1), dtype=np.int32)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

def run_lcs():
    rng = np.random.default_rng(12345)
    n = 30_000
    #a: npt.NDArray[np.int32]  = rng.integers(0, 100, n, dtype=np.int32)
    a: IntArray = rng.integers(0, 100, n, dtype=np.int32)
    b: IntArray = rng.integers(0, 100, n, dtype=np.int32)
    s = lcs(a,b)
    print(s)

def main():
    run_lcs()

if __name__ == "__main__":
    main()
