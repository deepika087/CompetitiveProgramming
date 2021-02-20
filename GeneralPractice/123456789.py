__author__ = 'deepika'


def step(s1, i):
    if i == 10:
        #if eval(s1) == 100:
        print s1, " = ", eval(s1)
        return
    if i != 1:
        step(s1 + '+' + str(i), i + 1)
        step(s1 + '-' + str(i), i + 1)
    step(s1 + str(i), i + 1)

step('', 1)


