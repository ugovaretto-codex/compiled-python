#!/usr/bin/env bash
#Python include and libraries must be in path
./clean.sh
cp lcs.py lcs_mypy.py
mypyc lcs_mypy.py
cythonize lcs.py
clang -shared lcs.c -Ofast -l python3.11 -o lcs.so
cythonize lcs_cython.py
clang -shared lcs_cython.c -Ofast -l python3.11 -o lcs_cython.so
cythonize lcs_cythonx.pyx
clang -shared lcs_cythonx.c -Ofast -l python3.11 -o lcs_cythonx.so
