def func1(x):
    return lambda: x**2


def func2(func1):
    return func1()

print("x**2")
x = int(input("Введите x: "))
print(func2(func1(x)))