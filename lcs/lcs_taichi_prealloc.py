import time
import sys
import taichi as ti
import numpy as np


ti.init(arch=ti.cpu)
def lcs(a: np.ndarray, b: np.ndarray) -> int:
    return _compute(a, b, dp)

@ti.kernel
def _compute(
    a: ti.types.ndarray(dtype=ti.int32),
    b: ti.types.ndarray(dtype=ti.int32),
    dp: ti.types.ndarray(dtype=ti.int32),
    ) -> int:
    ti.loop_config(serialize=True)
    for i in range(1, a.shape[0]+1):
        for j in range(1, b.shape[0]+1):
            if a[i-1] == b[j-1]:
                dp[i,j] = dp[i-1, j-1]+1
            else:
                dp[i,j] = ti.max(dp[i-1,j], dp[i, j-1])
    return dp[a.shape[0], b.shape[0]]


def run_lcs(n: int):
    rng = np.random.default_rng(1234567)
    a = rng.integers(0, 100, n, dtype=np.int32)
    b = rng.integers(0, 100, n, dtype=np.int32)
    tic = time.perf_counter() 
    lcs(a,b)
    toc = time.perf_counter()
    print(f"Taichi prealloc,{n},{toc - tic:0.4f}")

def main(n: int):
    global dp
    dp = np.ndarray(dtype=np.int32, shape = (n+1, n+1))
    run_lcs(n)

if __name__ == "__main__":
    n = 40_000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    main(n)
