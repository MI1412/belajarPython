from collections import deque
# bagus buat handling list
# NAME
#     collections
data = [data for data in range(10)]
d = deque(data)
print(d)
print(type(data))
print(type(d))
d.append("data  baru")
print(f"data baru: {d.pop()}")
print(f"pop left: {d.popleft()}")

