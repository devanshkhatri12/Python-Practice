# yield -> yeh bhi value return krta h, memory m us function ko rkhta h, sath m function ki state ko bhi rkhta h.

def evenGenerator(limit):
    for i in range(2, limit + 1, 2):
        yield i

    
for i in evenGenerator(10):
    print(i)


    # yield keyword is used to return a list of values from a function.