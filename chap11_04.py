
f = open('cp.txt', 'wt')
f.write('freshman\n')
f.write('sophomore\n')
f.write('junior\n')
f.write('senior\n')
f.close()

f = open('cp.txt', mode='r')
grade = f.readlines()
for i, g in enumerate(grade, start = 1):
    print('{}학년 {}'.format(i, g), end = '')
f.close()



