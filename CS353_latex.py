__author__ = 'deepika'


target = open('Combined_Exam_without_solutions.tex', 'w+')
ignore = False
for line in open("Combined_Exam.tex"):
    if ("begin{solution}" in line):
        ignore=True
    elif ("end{solution}" in line):
        ignore=False
    elif (not ignore):
        target.write(line)

print "Done"