
# 
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you"d like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
# 
# Enjoy your interview!
# 
# """
# You"re running a pool of servers where the servers are numbered sequentially starting from 1. Over time, any given server might explode, in which case its server number is made available for reuse. When a new server is launched, it should be given the lowest available number.
# 
# Write a function which, given the list of currently allocated server numbers, returns the number of the next server to allocate. In addition, you should demonstrate your approach to testing that your function is correct. You may choose to use an existing testing library for your language if you choose, or you may write your own process if you prefer.
# 
# For example, your function should behave something like the following:
# 
#   >> next_server_number([5, 3, 1])
#   2
#   >> next_server_number([5, 4, 1, 2])
#   3
#   >> next_server_number([3, 2, 1])
#   4
#   >> next_server_number([2, 3])
#   1
#   >> next_server_number([])
#   1
#   >>next_server_number([2])
# >>next_server_number([2, 2])
# """

def removeDuplicates(serversDuplicate):
    result = set()
    for i in serversDuplicate:
        if i in result:
            continue
        else:
            result.add(i)
    return list(result)

def binarySearch(arr, item_to_look_for, left, right):
    if left > right:
        return -1
    mid = right - (right - left)/2
    
    if arr[mid] == item_to_look_for:
        return mid
    elif arr[mid] > item_to_look_for:
        return binarySearch(arr, item_to_look_for, left, mid - 1)
    return binarySearch(arr, item_to_look_for, mid + 1, right)

def next_server_number(servers):
    servers = list(filter(lambda x: x > 0, servers))
    if len(servers) == 0:
        return 1
        
    if len(servers) == 1:
        if servers[0] == 1:
            return 2
        else:
            return 1
        
    serversDuplicate = sorted(servers)
    servers = removeDuplicates(serversDuplicate)
    max_server = servers[len(servers) - 1]
    for i in range(1, max_server + 1):
        result = binarySearch(servers, i, 0, len(servers) - 1)
        if result == -1:
            return i
        else:
            continue
    return max_server + 1
        
print "Running assertions"
assert next_server_number([-3]) == 1
assert next_server_number([3]) == 1
assert next_server_number([-5, 3, 1]) == 2
assert next_server_number([5, 5, 3, 1]) == 2
assert next_server_number([5, 3, 1]) == 2
assert next_server_number([5, 4, 1, 2]) == 3
assert next_server_number([3, 2, 1]) == 4
assert next_server_number([2, 3]) == 1
assert next_server_number([]) == 1
assert next_server_number([2]) == 1
print  "assertions ends"




"""
>> tracker = Tracker.new()
>> tracker.allocate("apibox")
"apibox1"
>> tracker.allocate("apibox")
"apibox2"
>> tracker.deallocate("apibox1")
nil
>> tracker.allocate("apibox")
"apibox1"
>> tracker.allocate("sitebox")
"sitebox1"
"""


class Tracker(object):
    def __init__(self):
        self.dictionary = {}
        
    def allocate(self, string):
        if string in self.dictionary:
            next_num = next_server_number(self.dictionary[string])
            self.dictionary[string].append(next_num)
            return string + str(next_num)
        else:
            self.dictionary[string] = [1]
            return string + str(1)
        
    def deallocate(self, string):
        
        serverName, serverNumber = self.splitCustom(string)
        
        if serverName not in self.dictionary:
            return None
        else:
            if int(serverNumber) in self.dictionary[serverName]:
                self.dictionary[serverName].remove(int(serverNumber))
            else:
                return None
        print self.dictionary
    
    def splitCustom(self, string):
        
        for i in range(len(string)):
            if string[i] >= "a" and string[i] <= "z":
                continue
            else:
                break
        
        return string[0:i], string[i:]
    
    def printDictionary(self):
        print "--------------RESULT---------------"
        print self.dictionary

tracker = Tracker()
print tracker.allocate("apibox")
print tracker.allocate("apibox")
tracker.deallocate("apibox1")
tracker.allocate("sitebox")
tracker.printDictionary()
print tracker.allocate("apibox")
print tracker.deallocate("abcbox100")
print tracker.deallocate("apibox100")
        