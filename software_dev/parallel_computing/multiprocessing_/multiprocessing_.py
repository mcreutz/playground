from multiprocessing import Pool, TimeoutError, cpu_count
import time
import os

def f(x):
    # time.sleep(1)
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # get number of CPUs
        print(cpu_count(), ' CPUs present\n')

        # print "[0, 1, 4,..., 81]"
        print('Ordered:')
        print(pool.map(f, range(10)))
        print('')

        # print same numbers in arbitrary order
        print('Unordered:')
        for i in pool.imap_unordered(f, range(10)):    
            print(i)
        print('')

        # evaluate "f(20)" asynchronously
        print('evaluate "f(20)" asynchronously')
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print(res.get(timeout=1))             # prints "400"
        print('')

        # evaluate "os.getpid()" asynchronously
        print('evaluate "os.getpid()" asynchronously')
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process
        print('')

        # launching multiple evaluations asynchronously *may* use more processes
        print('launching multiple evaluations asynchronously *may* use more processes')
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])
        print('')

        # make a single worker sleep for 10 secs
        print('make a single worker sleep for 10 secs')
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")
            print('')

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")