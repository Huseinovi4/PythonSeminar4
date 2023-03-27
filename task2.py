N = int(input())
array = list()
for i in range(N):
    number_of_berries = int(input())
    array.append(number_of_berries)

array_count = list()
for i in range(len(array)-1):
    array_count.append(array[i-1] + array[i] + array[i+1])
array_count.append(array[-2] + array[-1] + array[0])
print(max(array_count))