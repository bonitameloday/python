
import pickle as pk

with open('worldcup.bin', mode='rb') as fromf, open('2018worldcup.bin', mode='wb') as tof:
    while True:
        one = fromf.read(1)
        if not one:
            break
        tof.write(one)

with open('2018worldcup.bin', mode='rb') as tof:
        tof1 = pk.load(tof)
        tof2 = pk.load(tof)
        
print(tof1)
print(tof2)









