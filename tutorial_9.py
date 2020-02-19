# Python Multiprocessing Tutorial: Run Code in Parallel Using the Multiprocessing Module


import time


def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done Sleeping for 1 second...")
    return ""


# do_something2 requires the seconds parameter to run
def do_something2(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    print(f"Done Sleeping for {seconds} second...")
    return ""


# do_something2 requires the seconds parameter to run and returns a value
def do_something3(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping for {seconds} second..."


def original_function():

    # Original function
    start = time.perf_counter()
    # Starting a counter to know the execution time of the script

    # Running in order like this, is called running synchronously as it is running one after the other
    print("Synchronous Code")
    print()

    for _ in range(2):
        # _ variable is a throw away variable in python, which has no actual use
        # print(do_something3(1.3))
        print(do_something())

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


# Difference between CPU bound and IO bound task
# CPU bound is when CPU makes delays to process something and we have to wait
# IO bound, same as CPU bound but here we wait for input and output operations to be completed
# example of IO bound task: reading and writing to the file system, network operations, downloading files online

# CPU bound task do not benefit from using threading
# Some program even run slow using threads because of the added overhead cost for creating and destroying different threads
# CPU bound task use multiprocessing and run the jobs in parallel instead

# How multiprocessing works?
# The code is spread out to run on multiple processors on the machine
# And the tasks are running at the same time in parallel on multiple processors unlike threading

# When to use threading or multiprocessing?
# It depends on what are task are we performing and the computer's hardware,
# Or if the task is a CPU bound task(multiprocessing) or IO bound task(threading)
import multiprocessing

# Manual Multiprocessing Method - the old way
def example_1():

    start = time.perf_counter()

    print("Manual Multiprocessing Method")
    print()

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # Start the processes
    p1.start()
    p2.start()

    # To tell the process that they have to finish before executing the rest of the code as they are dependant on the process completion
    # Output when not using process.join()
    # Process take longer to spin up than threads
    """
    Manual Multiprocessing Method
    Finished in 0.01 second(s)

    Sleeping for 1 second...
    Sleeping for 1 second...
    Done Sleeping for 1 second...
    Done Sleeping for 1 second...
    """
    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


def example_2():

    start = time.perf_counter()

    print("Multiple parallel jobs using Manual Multiprocessing Method")
    print()

    # Keep track of all processes running
    processes = []
    for _ in range(10):
        # Even though the computer does not have 10 cores,
        # The CPU has ways of switching between cores when one of them is not too busy
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    # Cannot run process.join() inside the loop as it will become same as synchronous code
    # End all process execution before continuing
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


def example_3():

    start = time.perf_counter()

    print("Multiple parallel jobs using Manual Multiprocessing Method")
    print("Using functions with arguments without return")
    print()

    # Keep track of all processes running
    processes = []
    for _ in range(10):
        # Even though the computer does not have 10 cores,
        # The CPU has ways of switching between cores when one of them is not too busy
        # For multiprocessing, the arguments must be able to be serialised using pickle
        # Serialising using pickle means we are converting python objects into a format that can be deconstructed and reconstructed in another python script
        p = multiprocessing.Process(target=do_something2, args=[1.5])
        p.start()
        processes.append(p)

    # Cannot run process.join() inside the loop as it will become same as synchronous code
    # End all process execution before continuing
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


# Code below will not work on windows and it will crash in windows CMD
# It crashes in vscode python debugger, I could not figure out why though
# It works fine in linux terminal

import queue


# def helper(queue, seconds):
#     queue.put(do_something3(seconds))


# def display_que(que):
#     while not que.empty():
#         result = que.get()
#         print(result)


def example_4():

    start = time.perf_counter()

    print("Multiple parallel jobs using Manual Multiprocessing Method")
    print("Using functions with arguments with return")
    print()

    # Queue for helper function
    que = queue.Queue()

    # Keep track of all processes running
    processes = []
    for _ in range(10):
        # Attempt of using same lambda expression logic as in the Threading tutorial (tutorial_8)
        # Attempt fails as there are some limitation in Python regarding pickling lambda expressions in windows
        # It works on linux
        p = multiprocessing.Process(
            target=lambda queue, seconds: queue.put(do_something3(seconds)), args=[que, 1.5]
        )

        # How to resolve the issue in windows?
        # Create a helper function which will do the same job that the lambda expression was doing
        # p = multiprocessing.Process(target=helper, args=[que, 1.5])
        p.start()
        processes.append(p)

    # Cannot run process.join() inside the loop as it will become same as synchronous code
    # End all process execution before continuing
    for process in processes:
        process.join()

    # Check thread's return value
    while not que.empty():
        result = que.get()
        print(result)
    # display_que(que)
    # I could not get it to display the return of the function do_something3
    """
    Multiple parallel jobs using Manual Multiprocessing Method
    Using functions with arguments with return

    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Sleeping for 1.5 second...
    Finished in 1.51 second(s)
    """

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


import concurrent.futures


def example_5():

    start = time.perf_counter()

    print("ProcessPool Executor Method")
    print()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Below is same as in Threading tutorial (tutorial_8)
        # Submit method schedule a function to be executed and returns a future object
        # Future object encapsulated the execution of the function and allows us to check in on it after it's been scheduled
        # Can check if it is running, or if it's done, or the result
        f1 = executor.submit(do_something3, 1.5)
        f2 = executor.submit(do_something3, 1.5)

        # Result method will wait for the function to complete and will get the return value of the function in submit
        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


def example_6():

    start = time.perf_counter()

    print("Multiple parallel jobs using ProcessPool Executor Method")
    print("Example 1")
    print()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # List comprehension
        results = [executor.submit(do_something3, 1.5) for _ in range(10)]

        # as_completed will display the return value of do_something function in real time as it completes a parallel job
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


def example_7():

    start = time.perf_counter()

    print("Multiple parallel jobs using ProcessPool Executor Method")
    print("Example 2")
    print()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [3, 2.5, 1.5, 1]
        results = [executor.submit(do_something3, sec) for sec in secs]

        # as_completed will display the return value of do_something function in real time as it completes a parallel job
        for f in concurrent.futures.as_completed(results):
            # The 1 second job will finish first then the 1.5, 2.5, 3 thus proving how as_completed works
            # as_completed will return the future object in the order that they completed
            print(f.result())
            """
            Sleeping for 3 second...
            Sleeping for 2.5 second...
            Sleeping for 1.5 second...
            Sleeping for 1 second...
            Done Sleeping for 1 second...
            Done Sleeping for 1.5 second...
            Done Sleeping for 2.5 second...
            Done Sleeping for 3 second...
            Finished in 3.02 second(s)
            """

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


def example_8():

    start = time.perf_counter()

    print("Multiple parallel jobs using ProcessPool Executor Method")
    print("Example 3")
    print()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [3, 2.5, 1.5, 1]

        # To return the results in the same order that they started, we use the map function
        # But they all ran concurrently and did not slow down
        results = executor.map(do_something3, secs)

        for result in results:
            print(result)
            """
            Sleeping for 3 second...
            Sleeping for 2.5 second...
            Sleeping for 1.5 second...
            Sleeping for 1 second...
            Done Sleeping for 3 second...
            Done Sleeping for 2.5 second...
            Done Sleeping for 1.5 second...
            Done Sleeping for 1 second...
            Finished in 3.02 second(s)
            """

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
    print()
    print()


def example_9():
    pass


# the main function will call all other functions so that they will be executed once
def main():
    original_function()
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()
    example_8()
    example_9()


# This needs to be added as a stopping condition on windows or else the program goes on a recursive loop till it crashes
# On linux it will work fine and will not require the function main() or this stopping condition
if __name__ == "__main__":
    main()
