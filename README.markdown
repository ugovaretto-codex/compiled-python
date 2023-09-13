# Compiled Python

Benchmarked the longest common subsequence algorithm with:

* CPython
* Cython
* Mypyc
* Numba
* Taichi

The algorithm was explicitly selected to test single-core performance, no point in running it on GPUs because
it's going to be slower than on the CPU.


Taichi is the fastest, Numba it's the easiest to use, Cython the most portable but does not have direct support for GPUs and solutions like [this one](https://developer.nvidia.com/blog/accelerating-python-on-gpus-with-nvc-and-cython) are required.

Not tested with *PyTorch* since `torch.compile` does not support Python 3.11 yet.
PyTorch looks very promising and can compile any Python code to CPU or GPU by invoking directly the compiler in the Python code:

```python
import torch
def foo(x, y):
    a = torch.sin(x)
    b = torch.cos(y)
    return a + b
opt_foo1 = torch.compile(foo)
print(opt_foo1(torch.randn(10, 10), torch.randn(10, 10)))
```
Not tested with *Codon* since I was not able to make it work on MacOS, also it's its own language built on top of a subset of Python
which requires to do things like:

```python
from python import numpy as np
```
and annotate regular Python code with a `@python` decorator.


Install all the above tools with `pip3 taichi mypy numba cython`.

`mypyc` is included in the `mypy` package.


A good description of the various platforms can be found in [this YouTube video](https://www.youtube.com/watch?v=umLZphwA-dw&ab_channel=DougMercer)

[Longest common subsequence algorithm description](https://www.programiz.com/dsa/longest-common-subsequence)

Build scripts are provided to build, clean and run the benchmnarks.

## Performance:


![Benchmarks](https://github.com/ugovaretto-codex/compiled-python/blob/main/results_40000.png)

![Speedup](https://github.com/ugovaretto-codex/compiled-python/blob/main/speedup_40000.png)

 __NOTE__: Required for Cython pyx: use typed indices for loops, __not__ using typed indices
 results in a slowdown of ~17x (55s vs 3s)

Both Cython and Mypyc support building with `setup.py`, refer to the documentation for details.

## Taichi

[Taichi](https://www.taichi-lang.org/) is by far the best, even faster than equivalent C++ code and has a full graphics rendering engine included
making it possible to simulate and visualise results inside a Jupyter notebook in real-time, compiling to all the
available platforms, including Apple Metal. It also includes one of the best frameworks I have seen for dealing with
sparse data, allowing the same code to work on both sparse and dense arrays. In the documentation, an example of how
to make the code scale on multiple nodes with mpi4py is provided.

Switching to any platform is achieved by simply adding a
```python
ti.init(arch=ti.cpu|metal|cuda|vulkan|dx11...)
```
statement at the beginning of the module.

It can use compute shaders directly making it possible to run on any graphics card of any vendor.

__Limitation__: it seems that the size of NDArrays supported is 2Gi-elements maximum; when trying to go
above thi limit an error is reported saying that `int64` indices are not yet supported.

Using Numpy's *NDArrays* seems to result in better performance in comparison to Taichi arrays.

## Cython

Invoke `cythonize lcs.py` or `cythonize lcs_cython.py` or `cythonize lcs_cython.pyx` then compile the generated
`.c` file with:

```sh
clang -shared -O3 <file.c> -l python -o <lcs.so or lcs_cython.so>
```
On MacOS set the `CPATH` variable to point to the include directory where `Python.h` resides and the
`LIBRARY_PATH` to the location of the `libpython3.*` library.

On Linux, it should be enough to just install the `libpython-dev` package.

Run with `python -c "from lcs import main; main()"` or use `lcs_cython` when building the `lcs_python` module.

## Mypyc

Just invoke `mypyc lcs.py` then run `python -c "from lcs import main; main()`

## Numba and Taichi

No pre-compilation is required, the code is annotated and jitted and executed on the fly just
run `python3 <file>`.
