import multiprocessing
import time

def task1():
    for i in range(3):
        print("Task 1:", i)
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2:", i)
        time.sleep(1)

if __name__ == "__main__":

    start = time.time()

    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print("Total time:", end - start)