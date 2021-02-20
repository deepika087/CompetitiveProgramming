__author__ = 'deepika'


"""
input:
rideDuration = 90
songDuration = {1,10,25,35,60}

output:
[2,3]
"""

class Solution:

    def formatSongs(self, songDuration):
        songs = []

        for i in range(len(songDuration)):
            songs.append( [songDuration[i], i])

        return songs

    def songPairs(self, rideDuration, songDuration):

        effectiveRideDuration = rideDuration - 30

        songs = self.formatSongs(songDuration)

        songs = list(filter(lambda x: x[0] < effectiveRideDuration, songs))

        sorted(songs, key=lambda x: x[0])

        result = []
        left = 0
        right = len(songs) - 1

        delta_so_far = float('inf')
        """
        Collapse the duplicate values of song duration. This implementation assumes that song duration are all unique.
        """

        while left < right and left >= 0 and right < len(songs):

            if abs(songs[left][0] + songs[right][0] - rideDuration) < delta_so_far:
                delta_so_far = abs(songs[left][0] + songs[right][0] - rideDuration)
                result = [  songs[left][1], songs[right][1] ]
                if songs[left][0] + songs[right][0] > rideDuration:
                    right -= 1
                else:
                    left += 1

            """
            The assumption that song duration are all unique helps us here.. because if we don't collapse the duplicate.
            Now how do we now if increment left or decrement right.
            elif abs(left[0] + right[0] - rideDuration) == delta_so_far:
                result.append( ( left[1], right[1]) )
            """
        return result

s=Solution()
print(s.songPairs(90, [70,10,25,35,60]))
print(s.songPairs(90, [1,10,25,35,60]))
print(s.songPairs(50, [1,2, 3, 4, 5, 6, 7, 8]))