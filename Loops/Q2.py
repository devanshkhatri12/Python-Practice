numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sum_of_even = 0

for num in numbers:
    if(num % 2 == 0):
        Sum_of_even += num

print(Sum_of_even)


# OR
# total no. of even numbers till n

n = 10
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print(sum_even)
