# Python Threading Tutorial: Run Code Concurrently Using the Threading Module


import time

# Original function
start = time.perf_counter()
# Starting a counter to know the execution time of the script


def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping for {seconds} second..."


# Running in order like this, is called running synchronously as it is running one after the other
print("Synchronous Code")
print()

for _ in range(2):
    # _ variable is a throw away variable in python, which has no actual use
    print(do_something(1))
    print()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
print()
print()

# Difference between CPU bound and IO bound task
# CPU bound is when CPU makes delays to process something and we have to wait
# IO bound, same as CPU bound but here we wait for input and output operations to be completed
# Example of IO bound task: reading and writing to the file system, network operations, downloading files online

# Benefits of using threading and concurrency
# Use threading for a lot of IO bound task as we have a lot of waiting for it's completion

# CPU bound task do not benefit from using threading
# Some program even run slow using threads because of the added overhead cost for creating and destroying different threads
# CPU bound task use multiprocessing and run the jobs in parallel instead

# How threading works?
# It does not run code at same time, it just give the illusion that it's running at the same time
# When IO bound tasks come to a point where we have to wait for an output to continue with the code execution
# With threading or concurrency, it is just going to move on with the script and execute other codes while the IO operations finish

# Manual Threading Method - the old way
import threading
import queue

start = time.perf_counter()

print("Manual Threading Method")
print()

# Queue is used to get the return of the function do_something
que = queue.Queue()

# this type of thread cannot return the value of the function
# t1 = threading.Thread(target=do_something, args=[1.5])

# the lambda function takes 2 parameter: queue, seconds
# the args will supply the values of the 2 parameters required by the lambda function: queue.put(do_something(seconds))
# the function will look like: que.put(do_something(1.5))
# que.put() will append the return value of the function into the que list
# later the que.put() can be retrived and it will contain the values of all the function which ran in threads

t1 = threading.Thread(
    # lambda expression
    target=lambda queue, seconds: queue.put(do_something(seconds)),
    args=[que, 1.5],
)

t2 = threading.Thread(
    target=lambda queue, seconds: queue.put(do_something(seconds)), args=[que, 1.5]
)

# Starts the thread
t1.start()
t2.start()

# To tell the threads that they have to finish before executing the rest of the code as they are dependant on the thread completion
# Output when not using thread.join()
"""
Sleeping for 1 second...
Sleeping for 1 second...

Finished in 0.0 second(s)

Done Sleeping...
Done Sleeping...
"""

t1.join()
t2.join()

# Check thread's return value
while not que.empty():
    result = que.get()
    print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
print()
print()


# Demonstrate its impact for many concurrent jobs
start = time.perf_counter()

print("Multiple concurrent jobs using Manual Threading Method")
print()

# Keep track of all threads running
threads = []
que = queue.Queue()

for _ in range(10):
    t = threading.Thread(
        target=lambda queue, seconds: queue.put(do_something(seconds)), args=[que, 1.5]
    )
    t.start()
    threads.append(t)

# End all thread execution before continuing
for thread in threads:
    thread.join()

# Check thread's return value
while not que.empty():
    result = que.get()
    print(result)


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
print()
print()


# ThreadPool Executor - new, easier and more efficient way
import concurrent.futures

print("ThreadPool Executor Method")
print()

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit method schedule a function to be executed and returns a future object
    # Future object encapsulated the execution of the function and allows us to check in on it after it's been scheduled
    # Can check if it is running, or if it's done, or the result
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)

    # Result method will wait for the function to complete
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
print()
print()


print("Multiple concurrent jobs using ThreadPool Executor Method")
print("Example 1")
print()

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # List comprehension
    results = [executor.submit(do_something, 1.5) for _ in range(10)]

    # as_completed will display the return value of do_something function in real time as it completes a concurrent job
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
print()
print()


print("Multiple concurrent jobs using ThreadPool Executor Method")
print("Example 2")
print()

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [3, 2.5, 1.5, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    # as_completed will display the return value of do_something function in real time as it completes a concurrent job
    for f in concurrent.futures.as_completed(results):
        # The 1 second job will finish first then the 1.5, 2.5, 3 thus proving how as_completed works
        # as_completed will return the future object in the order that they completed
        print(f.result())

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
print()
print()


print("Multiple concurrent jobs using ThreadPool Executor Method")
print("Example 3")
print()

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [3, 2.5, 1.5, 1]
    # To return the results in the same order that they started, we use the map function
    # But they all ran concurrently and did not slow down
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
print()
print()
