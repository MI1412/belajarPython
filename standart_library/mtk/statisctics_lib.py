import statistics as stsc
# NAME
#     statistics - Basic statistics module.
angka = [data for data in range(10)]

mean = stsc.mean(angka)
median = stsc.median(angka)
variance = stsc.variance(angka)

print(mean)
print(median)
print(variance)
