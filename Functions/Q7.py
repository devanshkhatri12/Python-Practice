def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(Firstname='Devansh', Middlename='Kumar', Lastname='Khatri')
print_kwargs(Firstname='Devansh')
print_kwargs(Firstname='Devansh', Lastname='Khatri')