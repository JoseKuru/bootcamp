import time

time_start = time.time()
count = 10 ** 6
numbers = []


for i in range(count):
    numbers.append(i)
numbers.reverse()
print(f'reverse method --> {time.time() - time_start} seconds')

time_start = time.time()
numbers = []

for i in range(count):
    numbers.insert(0, i)
print(f'insert method ---> {time.time() - time_start} seconds')

