__author__ = 'deepika'

def socool(tasks, coolTime):
  cooldown = {}
  time = 0
  for task in tasks:
    if task not in cooldown:
      cooldown[task] = coolTime  #A -> 2
      for key in cooldown.keys(): #A -> 0, B -> 0
        if cooldown[key] > 0:
          cooldown[key] -= 1
      time += 1
    else:
      while cooldown[task] > 0:
        for key in cooldown.keys(): #A -> 0, B -> 0
          if cooldown[key] > 0:
            cooldown[key] -= 1
        time += 1
      time += 1
  time += 1
  return time


def magicFunc(a = []):
  a.append("1")
  print(a)

magicFunc()
magicFunc(["2"])

#print(socool(['A', 'A', 'B', 'A', 'B' ], 2))
#print(socool(['A', 'B', 'B', 'A', 'B' ], 2))
#print(socool(['A', 'B', 'A', 'C', 'B'], 2))