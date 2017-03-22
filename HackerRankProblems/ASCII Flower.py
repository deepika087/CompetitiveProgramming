__author__ = 'deepika'

line1 = "..O.."
line2 = "O.o.O"
line3 = "..O.."


r,c = raw_input().strip().split(' ')
r,c = [int(r),int(c)]

effectiveLine1 = line1 * c
effectiveLine2 = line2 * c
effectiveLine3 = line3 * c

for _ in range(r):
    print effectiveLine1
    print effectiveLine2
    print effectiveLine3

