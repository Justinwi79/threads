"""
Name: Harold Justin Windham
Date: 11/6/2022
Assignment: Module 11: Using Threads
Due Date: 11/6/2022
About this project: Estimate pi using random integers in threads
Assumptions: N/A
All work below was performed by Harold Justin Windham
"""

"""
References: Dr. Works modules and course videos. 
"""

import random
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


def task(n):  # Monte Carlo method provided by Dr. Works
    print("Processing {}".format(n))
    NumInCircle = 0
    NumTosses = random.randint(1000, 10000)
    for i in range(NumTosses):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # print("(", x, ",", y, ")")
        distSq = x * x + y * y
        if (distSq <= 1):
            NumInCircle += 1

    piEst = 4 * NumInCircle / NumTosses
    print("PI Est", piEst)


def main():
    print("Starting ThreadPoolExecutor\n")
    tosses = random.sample(range(1000, 10000), 100)  # generate random tosses between 1000 and 10000
    listn = list(tosses)  # list of 100 random tosses
    start = time.time()  # start timing execution
    with ThreadPoolExecutor(max_workers=3) as executor:  # distribute task function
        task1 = executor.submit(task, (0))
        time.sleep(1)  # slow down execution for alignment
        task2 = executor.submit(task, (1))
        time.sleep(1)
        task3 = executor.submit(task, (2))
        time.sleep(1)
    elapsed = time.time() - start  # stop timing execution
    print("\nPrimes task took %f sec. " % (elapsed))  # print time of execution
    print("\nAll tasks complete\n")
    for future in concurrent.futures.as_completed([task1, task2, task3]):
        print("Result of Task: {}".format(future.result()))
    print("\nList of Random Tosses")
    # for i in listn:  # print the list of random tosses
      #  print(i)


if __name__ == '__main__':
    main()



"""
/Users/justinwindham/PycharmProjects/threads/venv/bin/python /Users/justinwindham/PycharmProjects/threads/thread.py
Starting ThreadPoolExecutor

Processing 0
PI Est 3.1355034065102196
Processing 1
PI Est 3.1271935132518456
Processing 2
PI Est 3.141868512110727

Primes task took 3.015496 sec. 

All tasks complete

Result of Task: None
Result of Task: None
Result of Task: None

List of Random Tosses
2130
8637
4100
8330
8288
4628
6353
9479
1452
6914
7988
8281
1273
9677
8376
3776
5467
2346
4971
4865
2060
8819
5074
1534
8932
9608
7678
9986
8706
7932
1417
3541
7320
1199
3010
9898
9790
4639
5378
7882
6034
4756
3785
1095
4083
9287
8204
1064
7475
4129
3467
1947
3663
3441
8654
4998
4102
9748
6413
1892
5704
3190
9000
6500
8319
5460
8753
1945
3860
4190
5867
4131
1591
4697
6734
6939
5299
9063
4696
3822
6324
3872
3813
6143
3884
2223
4179
3259
7893
8007
6703
2523
9219
7173
9893
5702
7343
6737
4496
9942

Process finished with exit code 0

"""