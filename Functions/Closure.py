# factory function or closure

def chaicode(num):
    def actual(x):
        return x ** num
    return actual


a = chaicode(2)
b = chaicode(3)

# print(chaicode(2))

print(a(2))
print(b(2))