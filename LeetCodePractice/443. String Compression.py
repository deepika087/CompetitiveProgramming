__author__ = 'deepika'


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        writer = -1
        reader = 0

        while reader < len(chars):
            reader_end = reader
            while reader_end + 1 < len(chars) and chars[reader_end] == chars[reader_end + 1]:
                reader_end = reader_end + 1
            if reader_end == reader:
                writer = writer + 1
                chars[writer] = chars[reader]
                reader = reader + 1
            else:
                writer = writer + 1
                chars[writer] = chars[reader]
                writer = writer + 1 # for actually writing the value of occurrence
                if reader_end - reader + 1 <= 9:
                    chars[writer] = str(reader_end - reader + 1)
                else:
                    num = list(str(reader_end - reader + 1))
                    while len(num):
                        chars[writer] = num.pop(0)
                        writer = writer + 1
                    writer = writer - 1
                reader = reader_end + 1
        if writer != -1:
            chars = chars[0:writer+1]
        print chars
        return len(chars)

s=Solution()
print s.compress(["a","a","b","b","c","c","c"])
print s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print s.compress(["a","b"])
print s.compress(["a","a","b","b","c","c","c"])
print s.compress(["a","a","a","b","b","a","a"])
print s.compress(["o","o","o","o","o","o","o","o","o","o"]) #o, 1, 0

