
import pickle as pk

wc = {2010 : '남아프리카공화국', 2014 : '브라질'}
win = ['스페인', '독일']

with open('worldcup.bin', mode='wb') as f:
    pk.dump(wc, f)
    pk.dump(win, f)

with open('worldcup.bin', mode='wb') as f:
    wc[2018] = '러시아'
    win.append('프랑스')
    pk.dump(wc, f)
    pk.dump(win, f)

with open('worldcup.bin', mode='rb') as f:
    wc1 = pk.load(f)
    win1 = pk.load(f)

print(wc1)
print(win1)




