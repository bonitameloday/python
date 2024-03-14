lst = ['freshman\n', 'sophomore\n', 'junior\n', 'senior\n']
with open('cp.txt', mode = 'w') as f:
    f.writelines(lst)
    f.close()

with open('cp.txt', mode = 'r') as f:
    grade = f.readlines()
    for i,g in enumerate(grade, start = 1):
        print('{}학년 {}'.format(i, g),end ='')
    f.close()
        
