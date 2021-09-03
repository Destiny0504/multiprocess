from multiprocessing import Pool,TimeoutError
import time
import os

from process_a import printing as pa
from process_b import printing as pb

if __name__ == "__main__":
    test_data = 20
    with Pool(processes=3) as pool:
        res = pool.apply_async(pa, (test_data,))      # runs in *only* one process
        test_data = res.get(timeout=0.1)
        print(res.get(timeout=1))      

        res = pool.apply_async(pb, (test_data,))
        test_data = res.get(timeout=0.1)

        res = pool.apply_async(pa, (test_data,))
        test_data = res.get(timeout=0.1)

        res = pool.apply_async(pb, (test_data,))
        test_data = res.get(timeout=0.1)

        res = pool.apply_async(pa, (test_data,))
        test_data = res.get(timeout=0.1)

        print('==================')
        print(test_data)

