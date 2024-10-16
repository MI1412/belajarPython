from heapq import heapify, heappop, heappush
# NAME
#     heapq - Heap queue algorithm (a.k.a. priority queue).

# ga bagus buat pemula
data = [data for data in range(10)]
heapify(data)
heappush(data,90)
print(data)
sequence = [heappop(data) for i in range(11)]
print(sequence)