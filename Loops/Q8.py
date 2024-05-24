number  = 31
isprime = True

if number > 1:
    for i in range(2, number):
        if(number % i) == 0:
            isprime  = False
            break

print(isprime)

