__author__ = 'deepika'

#
# Your previous Plain Text content is preserved below:
#
# // RATE LIMITER
# // Write a accept_request function that returns true if we want to
# // accept a request, false if we're over the quota and we need to drop it.
# // We want to limit the number of requests to ANY URL at RATE req/sec.
# //
# // NOTES
# // - global variables survive between requests
# // - the rate limit is per url
# //
# // example
# // RATE = 2
# // t=0s   /home   --> true
# // t=0.1s /home --> true
# // t=0.2s /home --> false
# // t=0.2s /business --> true
# // t=1.1s /home --> true
#

# hashmap - key: url, startTime , endTime, count
#     key , list<timestamps>

#1 -> M posi
#N -> N*M

dictionary = dict()
def accept_request(url, current_time):
    if url not in dictionary:
        dictionary[url] = [current_time]
        return True
    else: #O(1)

        if (len(dictionary[url]) < 2): #O(1)
            dictionary[url].append(current_time)
            #print "For current time returning true", current_time
            return True
        else:
            most_latest = dictionary[url][-2] #O(1)
            # print "Reaching here: ", pop1, pop2
            if (current_time - most_latest < 1):
                # print dictionary
                return False
            else:
                dictionary[url].append(current_time) #O(1)
                # print dictionary
                return True

print accept_request('/home', 0.0)
print accept_request('/home', 0.1)
print accept_request('/home', 0.2)
print accept_request('/business', 0.2)
print accept_request('/home', 1.1)