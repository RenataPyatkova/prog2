
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
import statistics as st

from time import perf_counter as pc
import concurrent.futures as future

# r.seed(1234)
# np.random.seed(1234)

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

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function  
     with future.ProcessPoolExecutor() as ex:
        list1 = list(ex.map(sphere_volume, [n for i in range(np)], [d for l in range(np)]))
        # processes=[]
        # results =[]
        # for _ in range(np): # intializing all the processes
        #     p = ex.submit(sphere_volume, n, d) 
        #     processes.append(p)
        #     # instead of waiting for each task to finish, we store all the Future objects in processes.
        # for i in processes: # getting results after the processes have all started
        #     r = i.result() 
        #     results.append(r)
        # print("all done")
     return st.mean(list1)#sum(results) / len(results)#st.mean(results)


# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    #np = the chuncks we split our data into
    with future.ProcessPoolExecutor() as ex:
        processes=[]
        results =[]
        for _ in range(np): # intializing all the processes
            p = ex.submit(sphere_volume, n//np, d) 
            processes.append(p)
            # instead of waiting for each task to finish, we store all the Future objects in processes.
        for i in processes: # getting results after the processes have all started
            r = i.result() 
            results.append(r)
        print("all done")
    return sum(results) / len(results)#st.mean(results) 



def main():
    n = 100000
    d = 11

    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
    '''Process took 21.32 seconds'''

    # part 1 -- parallelization of a for loop among 10 processes
    start = pc()
    sphere_volume_parallel1(n,d,10)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
    '''Process took 14.64 seconds'''

    # part 2
    start = pc()
    sphere_volume_parallel2(n,d,10)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
    '''Process took 3.01 seconds'''






if __name__ == '__main__':
	main()
