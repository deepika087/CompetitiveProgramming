# Definition for an interval.
"""
Not complete passes 50% of test cases but not all. Problem is assumption is that overlapping will i+1 elemtn but it could be i+@ element too.
Ex (-100, -98), (-99, -97), (-98, -96)
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ")"

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        if (len(intervals) == 1):
            return  [-1]

        intervalDict = dict()
        for i in range(len(intervals)):
            intervalDict[intervals[i]] = i
        intervals = sorted(intervals, key=lambda x: x.start)
        result = [ -1 for i in range(len(intervals))]
        print " After sorting : ", intervals
        for i in range(len(intervals)):
            if (i == len(intervals) - 1):
                pass
            else:
                first = intervals[i]
                second = intervals[i+1]
                if (first.end <= second.start or (first.end < 0 and second.start < 0 and -first.end <= -second.start)):
                    result[intervalDict[intervals[i]]] = intervalDict[intervals[i+1]]
        return result

s=Solution()
print s.findRightInterval([Interval(-100,-98),Interval(-99,-97),Interval(-98,-96),Interval(-97,-95),Interval(-96,-94),Interval(-95,-93),Interval(-94,-92),Interval(-93,-91),Interval(-92,-90),Interval(-91,-89),Interval(-90,-88),Interval(-89,-87),Interval(-88,-86),Interval(-87,-85),Interval(-86,-84),Interval(-85,-83),Interval(-84,-82),Interval(-83,-81),Interval(-82,-80),Interval(-81,-79),Interval(-80,-78),Interval(-79,-77),Interval(-78,-76),Interval(-77,-75),Interval(-76,-74),Interval(-75,-73),Interval(-74,-72),Interval(-73,-71),Interval(-72,-70),Interval(-71,-69),Interval(-70,-68),Interval(-69,-67),Interval(-68,-66),Interval(-67,-65),Interval(-66,-64),Interval(-65,-63),Interval(-64,-62),Interval(-63,-61),Interval(-62,-60),Interval(-61,-59),Interval(-60,-58),Interval(-59,-57),Interval(-58,-56),Interval(-57,-55),Interval(-56,-54),Interval(-55,-53),Interval(-54,-52),Interval(-53,-51),Interval(-52,-50),Interval(-51,-49),Interval(-50,-48),Interval(-49,-47),Interval(-48,-46),Interval(-47,-45),Interval(-46,-44),Interval(-45,-43),Interval(-44,-42),Interval(-43,-41),Interval(-42,-40),Interval(-41,-39),Interval(-40,-38),Interval(-39,-37),Interval(-38,-36),Interval(-37,-35),Interval(-36,-34),Interval(-35,-33),Interval(-34,-32),Interval(-33,-31),Interval(-32,-30),Interval(-31,-29),Interval(-30,-28),Interval(-29,-27),Interval(-28,-26),Interval(-27,-25),Interval(-26,-24),Interval(-25,-23),Interval(-24,-22),Interval(-23,-21),Interval(-22,-20),Interval(-21,-19),Interval(-20,-18),Interval(-19,-17),Interval(-18,-16),Interval(-17,-15),Interval(-16,-14),Interval(-15,-13),Interval(-14,-12),Interval(-13,-11),Interval(-12,-10),Interval(-11,-9),Interval(-10,-8),Interval(-9,-7),Interval(-8,-6),Interval(-7,-5),Interval(-6,-4),Interval(-5,-3),Interval(-4,-2),Interval(-3,-1),Interval(-2,0),Interval(-1,1),Interval(0,2),Interval(1,3),Interval(2,4),Interval(3,5),Interval(4,6),Interval(5,7),Interval(6,8),Interval(7,9),Interval(8,10),Interval(9,11),Interval(10,12),Interval(11,13),Interval(12,14),Interval(13,15),Interval(14,16),Interval(15,17),Interval(16,18),Interval(17,19),Interval(18,20),Interval(19,21),Interval(20,22),Interval(21,23),Interval(22,24),Interval(23,25),Interval(24,26),Interval(25,27),Interval(26,28),Interval(27,29),Interval(28,30),Interval(29,31),Interval(30,32),Interval(31,33),Interval(32,34),Interval(33,35),Interval(34,36),Interval(35,37),Interval(36,38),Interval(37,39),Interval(38,40),Interval(39,41),Interval(40,42),Interval(41,43),Interval(42,44),Interval(43,45),Interval(44,46),Interval(45,47),Interval(46,48),Interval(47,49),Interval(48,50),Interval(49,51),Interval(50,52),Interval(51,53),Interval(52,54),Interval(53,55),Interval(54,56),Interval(55,57),Interval(56,58),Interval(57,59),Interval(58,60),Interval(59,61),Interval(60,62),Interval(61,63),Interval(62,64),Interval(63,65),Interval(64,66),Interval(65,67),Interval(66,68),Interval(67,69),Interval(68,70),Interval(69,71),Interval(70,72),Interval(71,73),Interval(72,74),Interval(73,75),Interval(74,76),Interval(75,77),Interval(76,78),Interval(77,79),Interval(78,80),Interval(79,81),Interval(80,82),Interval(81,83),Interval(82,84),Interval(83,85),Interval(84,86),Interval(85,87),Interval(86,88),Interval(87,89),Interval(88,90),Interval(89,91),Interval(90,92),Interval(91,93),Interval(92,94),Interval(93,95),Interval(94,96),Interval(95,97),Interval(96,98),Interval(97,99),Interval(98,100),Interval(99,101)])
print s.findRightInterval([Interval(-99,-97), Interval(-100,-98),Interval(-98,-96),Interval(-97,-95),Interval(-96,-94),Interval(-95,-93),Interval(-94,-92),Interval(-93,-91),Interval(-92,-90),Interval(-91,-89),Interval(-90,-88)])
print s.findRightInterval([ Interval(-2,-1), Interval(-10,-9), Interval(-4,-3) ])
print s.findRightInterval([ Interval(1,4), Interval(2,3), Interval(3,4) ])
print s.findRightInterval([ Interval(3,4), Interval(2,3), Interval(1,2) ])