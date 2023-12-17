"""
Name: Harold Justin Windham
Date: 11/27/2022
Assignment: Module 14: Python Dask Multi Task Script
Due Date: 11/27/2022
About this project: Use distributed and parallel computing to calculate pi
Assumptions: N/A
All work below was performed by Harold Justin Windham
"""

"""
References: Dr. Works modules and course videos. 
"""

import random

from dask.distributed import LocalCluster, Client

cluster = LocalCluster()
client = Client(cluster)

#  print(client.scheduler_info()['services'])


def plus(x):
    return 1 / x


def minus(x):
    return -1 / x


def calc(n):  # calculate pi
    sum = 0
    for i in range(n):
        term = (-1) ** i / (2 * i + 1)
        sum = sum + term

    return sum * 4


def calcs(n):
    sum = 0
    for i in range(n):
        term = minus(i), plus(i)
        sum = sum + term

    return sum * 4


def main():
    ran = random.randint(1, 1000)
    ran1 = random.randint(3, 1003)

    ran2 = random.randint(1, 1000)
    ran3 = random.randint(3, 1003)

    pi = calc(ran)
    pi1 = calc(ran1)

    pi2 = (plus(ran) + minus(ran2)) * 4
    pi3 = calc(ran3)

    print("Pi = ", pi)
    print("Pi1 = ", pi1)

    print("Pi2 = ", pi2)
    print("Pi3 = ", pi3)


if __name__ == '__main__':
    main()

"""
/Users/justinwindham/PycharmProjects/threads/venv/bin/python /Users/justinwindham/PycharmProjects/threads/dask.py
Pi =  3.1760651768684385
Pi1 =  3.1427705094828036
Pi2 =  0.13390688961354333
Pi3 =  3.140072897628418

Process finished with exit code 0
"""


