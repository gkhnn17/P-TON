
import multiprocessing
import time
 
def cube(x):
    return x**3
 
if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    start_time = time.perf_counter()
    processes = [pool.apply_async(cube, args=(x,)) for x in range(1,1000)]
    result = [p.get() for p in processes]
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")
    print(result)





"""import multiprocessing
import time
 
def task():
    print('Sleeping for 0.5 seconds')
    time.sleep(1)
    print('Finished sleeping')
 
if __name__ == "__main__":
    start_time = time.perf_counter()
 
    # Creates two processes
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
 
    # Starts both processes
    p1.start()
    p2.start()
    p1.join()#join olmasa print başta yazılacak
    p2.join()
    finish_time = time.perf_counter()
 
    print(f"Program finished in {finish_time-start_time} seconds")"""