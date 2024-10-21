
"""
Solutions to module 4
Review date:
"""

student = "Renata Piatkova"
reviewer = ""

import math as m
import random as r
import numpy as np
import functools

r.seed(1234)
np.random.seed(1234)

def sphere_volume(n, d):
    # n is the number of random points to generate 
    # d is the number of dimensions
    points = [tuple(np.random.uniform(-1, 1, d)) for i in range(n)] # inside a cube
    sphere = list(filter(lambda x: x<=1, [functools.reduce(lambda x,y : x+y, map(lambda x: x**2, i)) for i in points]))
    # the fraction of points that lie inside the hypersphere should approximate 
    # the ratio of the hypersphere's volume to the cube's volume
    # (2r)**d = cube's volume
    volume = (len(sphere)/n) * (2**d)
    return volume

def hypersphere_exact(n,d):
    return ((m.pi)**(d/2))/m.gamma((d/2)+1)
     
def main():
    n_list = [100000, 100000]
    d_list = [2, 11]
    for n,d in zip(n_list,d_list):
        print(f'The estimated volume is {sphere_volume(n,d)} \n'
            f'The actual volume is {hypersphere_exact(n,d)}')


if __name__ == '__main__':
	main()
