
given_age = input("Give Your age: ")
age = int(given_age)

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")