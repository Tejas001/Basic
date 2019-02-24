def zero(x):
    try:
        return 10/x
    except ZeroDivisionError:
        print("Division by zero")

print(zero(2))
print(zero(0))
print(zero(1))




