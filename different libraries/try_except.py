def f(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Zero division :( ')
    else:
        print('result is', result)
    finally:
        print('final')

print(f(5, 0))
print(f(5, 1))
print(f(5, []))
