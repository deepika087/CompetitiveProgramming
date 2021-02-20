__author__ = 'deepika'

#Roman numbers
def valueof(c):
   v = {'M':1000, 'C':100, 'V':5, 'I':1, 'X':10, 'D':500, 'L':50}
   return v[c]

"""
map<char, int> vals = { {'I', 1},
                        {'V', 5},
                        {'X', 10},
                        {'L', 50},
                        {'C', 100},
                        {'D', 500},
                        {'M', 1000}
                    };

Try this too. It is simpler.
def romanToInt(string s){
    int res = vals[s[s.size() - 1]];
    for (int i = s.size() - 2; i >= 0; i--) {
        if (vals[s[i]] < vals[s[i+1]])
            res -= vals[s[i]];
        else
            res += vals[s[i]];
    }
    return res;
}
"""
def rom2int(roman):
  if len(roman) == 1:
      return valueof(roman)

  tmp = 0
  ret = 0
  last = valueof(roman[0])
  if valueof(roman[1]) >= last:
    tmp = last
  else:
    ret = last

  for c in roman[1:]:
    v = valueof(c)
    if v > last:
      ret += v - tmp
      tmp = 0
    elif v == last:
      ret += v + tmp
      tmp = 0
    else:
      ret += tmp
      tmp = v
    last = v
  return ret + tmp



def int2Rom(input):
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000,   900, 500,  400, 100,  90,   50 , 40,   10,   9,   5,    4,    1]

    i = 0
    result = ""
    while input:
        if input - values[i] >= 0:
            result += numerals[i]
            input = input - values[i]
        else:
            i = i + 1
    return result


#print "INT2ROM" , int2Rom(64)

print rom2int(int2Rom(4))
print rom2int(int2Rom(64))
print rom2int(int2Rom(69))
