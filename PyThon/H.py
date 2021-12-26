# Queue task
import heapq
# from sys import intern
# from random import randint
# from time import time

"""
def time_estimator2(lenght, offices, times):
    traffic = dict()
    for aux in range(offices):
        # intern is my attempt to boost program runtime
        traffic[intern(str(aux))] = times[aux]

    for idx in range(offices, lenght):
        # free office is the key of the lowwest element in dict
        free_office = min(traffic, key=traffic.get)
        traffic[free_office] += times[idx]

    return max(traffic.values())
"""

"""
def time_estimator3(length, offices, times):
    heap = list()
    for aux in range(offices):
        heapq.heappush(heap, times[aux])
    
    for idx in range(offices, length):
        heap[0] += times[idx]
        heapq.heapify(heap)
        

    return heapq.nlargest(1, heap)[0]
"""

def time_estimator(length, offices, times):
    heap = list()
    for aux in range(offices):
        heapq.heappush(heap, times[aux])

    for idx in range(offices, length):
        heap[0] += times[idx]
        heapq.heapify(heap)
        

    return heapq.nlargest(1, heap)[0]

n, k = map(int, input().split())
passengers = list(map(int, input().split()))

# n, k = 100000, 1000
# passengers = [randint(1, 10000) for _ in range(n)]

# now = time()
print(time_estimator(n, k, passengers))
# print(time() - now)
# now = time()
# print(time_estimator2(n, k, passengers))
# print(time() - now)