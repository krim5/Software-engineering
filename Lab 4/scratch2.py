import math


def z(x, y):
    return (math.sin(2*x) ** 2 + math.cos(y) ** 2) * 2


x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(z(x, y))
