# WARNING: Taichi always print to standard output the following lines:
# [Taichi] version 1.6.0, llvm 15.0.7, commit f1c6fbbd, osx, python 3.11.5
# [Taichi] Starting on arch=arm6
# it is therefore required to filter out the first two lines of output
# invoke as
#
# python3 lcs_taichi.py 10000 | tail -n +3
#
# print output starting from third line

# Using Numpy NDArrays is faster than Taichi NDArrays
# invokde with 'python3 lcs_taichi.py [size] [true for Taichi arrays | false for Numpy] 
# defaults are size=40000 and Taichi arrays

import sys
import time
import taichi as ti
import numpy as np
ti.init(arch=ti.cpu)

def lcs(a: np.ndarray, b: np.ndarray, use_ti_ndarray: bool) -> int:
    if not use_ti_ndarray:
        dp = np.ndarray(
                shape=(len(a)+1, len(b)+1),
                dtype=np.int32
        )
        return _compute(a, b, dp)
    else:
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


def run_lcs(n: int, use_ti_ndarray: bool):
    rng = np.random.default_rng(1234567)
    a = rng.integers(0, 100, n, dtype=np.int32)
    b = rng.integers(0, 100, n, dtype=np.int32)
    tic = time.perf_counter()
    lcs(a,b, use_ti_ndarray)
    toc = time.perf_counter()
    array_type = "(Taichi NDArray)" if use_ti_ndarray else "(Numpy NDArray)"
    print(f"Taichi {array_type},{n},{toc - tic:0.4f}")

def main(n: int, use_ti_ndarray: bool):
    run_lcs(n, use_ti_ndarray)

if __name__ == "__main__":
    n = 40_000
    use_ti_ndarray = True
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    if len(sys.argv) == 3:
        use_ti_ndarray = sys.argv[2].lower() == "true"
    main(n, use_ti_ndarray)
