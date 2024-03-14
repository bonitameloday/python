def divide(x,y):
    result = x / y
    return result

try:
    result1 = divide(3.2, 2)
    result2 = divide(5.4, 0)

except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다.')

else:
    pass
print('결과: ', result1)
    
