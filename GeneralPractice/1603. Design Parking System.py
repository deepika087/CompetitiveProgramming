__author__ = 'deepika'

"""
Details
Runtime: 124 ms, faster than 90.24% of Python online submissions for Design Parking System.
Memory Usage: 13.9 MB, less than 99.80% of Python online submissions for Design Parking System.
"""

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.bigSpots = big
        self.mediumSpots = medium
        self.smallSpots = small
        self.bigCurrent = 0
        self.mediumCurrent = 0
        self.smallCurrent = 0


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.bigCurrent < self.bigSpots:
                self.bigCurrent += 1
                return True
            return False
        elif carType == 2:
            if self.mediumCurrent < self.mediumSpots:
                self.mediumCurrent += 1
                return True
            return False
        else:
            if self.smallCurrent < self.smallSpots:
                self.smallCurrent += 1
                return True
            return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)