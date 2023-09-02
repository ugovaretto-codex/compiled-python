#!/usr/bin/env bash
size=10000
if [[ "$#" -eq 1 ]]; then
  size=$1
fi
python3 ./lcs.py $size 
python3 -c "from lcs_mypy import main; main($size, 'Mypy')"
python3 -c "from lcs import main; main($size, 'Cython')"
python3 -c "from lcs_cython import main; main($size)"
python3 -c "from lcs_cythonx import main; main($size)"
python3 lcs_numba.py $size
python3 lcs_taichi.py $size | tail -n +3
python3 lcs_taichi_prealloc.py $size | tail -n +3
./lcs_cpp.exe $size
