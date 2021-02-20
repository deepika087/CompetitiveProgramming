__author__ = 'deepika'


class File:
    def __init__(self, nm, size):
        self.name = nm
        self.size = size

    def __str__(self):
        return "[ " + self.name + " " + str(self.size) + "GB ]"
    def __repr__(self):
        return self.__str__()


class Critera:

    def meetCondition(self, files):
        pass


class NameCritera(Critera):

    def __init__(self, extension):
        self.extension = extension

    def meetCondition(self, files):

        return list(filter(lambda x: self.extension in x.name, files)) #This xml can be customized as well rather than hardcoding it.

class SizeCritera(Critera):

    def __init__(self, size):
        self.size = size

    def meetCondition(self, files):

        return list(filter(lambda x: x.size > self.size, files))

class AndCriteria:

    def __init__(self, cr1, cr2):
        self.cr1 = cr1
        self.cr2 = cr2

    def apply(self, files):
        intermediate_output = self.cr1.meetCondition(files)

        return self.cr2.meetCondition(intermediate_output)

class OrCriteria:

    def __init__(self, cr1, cr2):
        self.cr1 = cr1
        self.cr2 = cr2

    def apply(self, files):
        output1 = self.cr1.meetCondition(files)
        output2 = self.cr2.meetCondition(files)

        for _o in output2:
            if _o not in output1:
                output1.append(_o)

        return output1
    

f1 = File("abc.txt", 10)
f2 = File("lmn.xml", 5)
f3 = File("pqr.xml", 15)
f4 = File("xyz.png", 20)

sizeCR1 = SizeCritera(5)
sizeCR2 = SizeCritera(15)
nameCR1 = NameCritera("xml")
nameCR2 = NameCritera("txt")

a1 = AndCriteria(sizeCR1, nameCR1)
o1 = OrCriteria(sizeCR2, nameCR2)

print(a1.apply([f1, f2, f3, f4]))
print(o1.apply([f1, f2, f3, f4]))

