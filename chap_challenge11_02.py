def divide(x,y):
    if y == 0:
        raise ZeroDivisionError('0으로는 나눌 수 없습니다.')
    return x/y

try:
    result = divide(3.2, 2)
    result1 = divide(5.4, 0)
except ZeroDivisionError as e:
    print(e)
else:
    pass
print('결과: {}'.format(result))
