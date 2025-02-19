age = 21
day = "Wednesday"

price = 12 if age >= 18 else 8
print(f"price is:", price)

if day == "Wednesday":
    price -= 2      #price after 2 dollar discount

print("Ticket price for U is: $",price)
