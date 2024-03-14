uyear = {1:'freshman', 2:'sophomore', 3:'junior', 4:'senior'}

try:
    grade = int(input('대학교 몇 학년이지요?'))
    if grade < 1 or grade > 4:
        raise Exception('1~4 정수를 입력하세요.')
except Exception as e:
    print("예외 발생 이름: ".format(type(e)))
    print("예외 발생 이유: ".format(e))
else:
    print('{}학년: {}'.format(grade, uyear[grade]))
finally:
    print('예외 처리가 잘되는군요!')
