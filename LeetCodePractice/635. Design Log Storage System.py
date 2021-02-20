__author__ = 'deepika'

"""
You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the
following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
Note:
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.
"""

class LogSystem(object):

    def __init__(self):
        self.data = {}


    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        if timestamp in self.data:
            self.data[timestamp].append(id)
        else:
            self.data[timestamp] = [id]

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        s, e = self._get_formatted_time(s, e, gra)
        print s, e
        result = []
        print self.data
        for (k, v) in self.data.items():
            if s <= k <= e :
                result += v
        return result


    def _get_formatted_time(self, s, e, granularity):
        if granularity == "Second":
            return s, e
        s = s.split(":")
        e = e.split(":")
        if granularity == "Minute":
            return ":".join(s[:-1]), ":".join(e[:-1])

        if granularity == "Hour":
            return ":".join(s[:-2]), ":".join(e[:-2])

        if granularity == "Day":
            return ":".join(s[:-3]), ":".join(e[:-3])

        if granularity == "Month":
            return ":".join(s[:-4]), ":".join(e[:-3])

        else:
            return s[0], e[0]


# Your LogSystem object will be instantiated and called as such:
obj = LogSystem()
obj.put(1, "2017:01:01:23:59:59");
obj.put(2, "2017:01:01:22:59:59");
obj.put(3, "2016:01:01:00:00:00");
print obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year");
print obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour");