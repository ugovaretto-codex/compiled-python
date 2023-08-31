
__First commit__, will fix and update with more information and diagrams.

# Compiled python

Tested the longest commons subsequence algorithm with:

* CPython
* Cython
* Mypyc
* Numba
* Taichi

Was not able to make *Codon* work on MacOS, also it's its own language built on top of a subset of python
which requires to do things like:

```python
from python import numpy as np
```
and annotate regular python code with a `@python` decorator.

[Taichi](https://www.taichi-lang.org/) is by far the best, even faster than equivalent C++ code and has a full graphics rendering enginge included
making it possible to simulate and visualise results inside a Jupyter notebook in real-time, compiling to all the
available platforms, including Apple Metal. It also include one of the best frameworks I have seen for dealing with
sparse data, allowing the same code to work on both sparse and dense arrays. In the documentation an example of how
to make the code scale on multiple nodes with mpi4py is provided.
Switching to any platform is achieved by simply adding a
```python
ti.init(arch=ti.cpu|metal|cuda|vulkan|dx11...)
```
statement at the beginning of the module.

It can use compute shaders directly making it possible to run on any graphics card of any vendor.

Install all the above tools with `pip3 taichi mypy numba cython`.

`mypyc` is included in the `mypy` package.


A good description of the various platforms can be found in [this YouTube video](https://www.youtube.com/watch?v=umLZphwA-dw&ab_channel=DougMercer)

[Longest common subsequence algorithm description](https://www.programiz.com/dsa/longest-common-subsequence)

Performance:

* CPython:   usr time  197.07 secs    0.19 millis  197.06 secs
* numpy: usr time  447.09 secs    0.19 millis  447.09 secs
* mypyc: usr time   24.92 secs    0.23 millis   24.92 secs
* vanilla cython: usr time   83.51 secs    0.24 millis   83.51 secs
* cython with type annotation: usr time   27.29 secs    0.24 millis   27.29 secs
* cython pyx: usr time    3.30 secs    0.28 millis    3.30 secs
* taichi: usr time    2.56 secs    0.21 millis    2.56 secs
* taichi static: usr time    2.46 secs    0.22 millis    2.46 secs
* numba: usr time    3.40 secs    0.21 millis    3.40 secs

 __NOTE__: Required for cypthon pyx: use typed indices for loops, __not__ using typed indices
 results in a slowdown of ~17x (55s vs 3s)

Both Cython and Mypyc support building with `setup.py`, refer to the documentation for details.


## Cython

Invoke `cythonize lcs.py` or `cythonize lcs_cython.py` or `cythonize lcs_cython.pyx` then compile the generted
`.c` file with:

```sh
clang -shared -O3 <file.c> -l python -o <lcs.so or lcs_cython.so>
```
On MacOS set the `CPATH` variable to point to the include directory where `Python.h` resides and the
`LIBRARY_PATH` to the location of the `libpython3.*` library.

On Linux it should be enough to just install the `libpython-dev` package.

Run with `python -c "from lcs import main; main()"` or use `lcs_cython` when building the `lcs_python` module.

## Mypyc

Just invoke `mypyc lcs.py` then run `python -c "from lcs import main; main()`

## Numba and Taichi

No pre-compilation required, the code is annotated and jitted and executed on the fly just
run `python3 <file>`.