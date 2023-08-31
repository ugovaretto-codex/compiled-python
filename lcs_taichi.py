import taichi as ti
import numpy as np
ti.init(arch=ti.cpu)

def lcs(a: np.ndarray, b: np.ndarray) -> int:
    dp = ti.ndarray(
            shape=(len(a)+1, len(b)+1),
            dtype=ti.i32
    )
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
