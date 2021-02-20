__author__ = 'deepika'
no_of_chars = 256

# Function to find smallest window
# containing all characters of 'pat'
def findSubString(string, pat):

    len1 = len(string)
    len2 = len(pat)

    # check if string's length is less than pattern's
    # length. If yes then no such window can exist
    if len1 < len2:

        print("No such window exists")
        return ""

    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars

    # store occurrence ofs characters of pattern
    for i in range(0, len2):
        hash_pat[ord(pat[i])] += 1

    start, start_index, min_len = 0, -1, float('inf')

    # start traversing the string
    count = 0 # count of characters
    for j in range(0, len1):
        print("Dealing with char: ", string[j])
        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1

        # If string's char matches with
        # pattern's char then increment count
        if (hash_pat[ord(string[j])] != 0 and
            hash_str[ord(string[j])] <= hash_pat[ord(string[j])]):
            print("increasing count")
            count += 1

        # if all the characters are matched
        if count == len2:
            print("Found prospect")
            # Try to minimize the window i.e., check if
            # any character is occurring more no. of times
            # than its occurrence in pattern, if yes
            # then remove it from starting and also remove
            # the useless characters.
            while (hash_str[ord(string[start])] >
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):

                if (hash_str[ord(string[start])] >
                    hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                    print("incrementing start to: ", start)
                start += 1

            # update window size
            len_window = j - start + 1
            if min_len > len_window:

                min_len = len_window
                start_index = start

    # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""

    # Return substring starting from
    # start_index and length min_len
    return string[start_index : start_index + min_len]

# Driver code
if __name__ == "__main__":

    string = "this is a test string"
    pat = "tist"

    print("Smallest window is : ")
    print(findSubString(string, pat))
