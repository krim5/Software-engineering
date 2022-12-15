def func1(n):
    return lambda x: (x+n)**2


print("(x+n)^2")
n = int(input("Введите число x: "))
x = int(input("Введите число n: "))
func = func1(n)
print(func(x))

