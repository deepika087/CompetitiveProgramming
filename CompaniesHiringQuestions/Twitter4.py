__author__ = 'deepika'


start = raw_input('')
end = raw_input('')
n = int(raw_input(''))

result = []
for i in range(n):
    data = raw_input('')
    if '    ' in data:
        datSplit = data.split('    ')
        dateData = datSplit[0]
        if dateData >= start and dateData <= end:
            result.append(data)
    else:
        if data >= start and data <= end:
            result.append(data)

for _d in result:
    print _d
