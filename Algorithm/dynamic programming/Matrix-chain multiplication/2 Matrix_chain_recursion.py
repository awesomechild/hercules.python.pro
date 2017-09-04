#-*- coding: utf-8 -*-
import sys, time
from functools import lru_cache
@lru_cache(maxsize = None)

def recursive_matrix_chain(p, i, j):
    ''' 计算第i到第j个矩阵链相乘的乘法次数 '''
    if i == j:
        return 0
    m = sys.maxsize
    for k in range(i, j):
        q = recursive_matrix_chain(p, i, k) + recursive_matrix_chain(p, k+1, j) + p[i-1]*p[k]*p[j]
        if q < m:
            m = q
    return m


def main():
    p = [30,35,15,5,10,20,25,5,16,34,28,19,66,34,78,55,23]
    print (recursive_matrix_chain(tuple(p), 1, len(p)-1))

if __name__ == '__main__':
    b = time.time()
    main()
    print ('total run time is:', time.time()-b)
