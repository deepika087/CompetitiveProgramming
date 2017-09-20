__author__ = 'deepika'
"""
Not working fine for last 5 inputs. I guess osme space issues is there.
"""

if __name__ =="__main__":
    string = raw_input('')
    n = int(raw_input(''))
    landmarks = raw_input('')
    landmarks = landmarks.split()

    for landmark in landmarks:
        #print " for landmark : ", landmark
        string = string.replace(landmark, "<b>" + landmark + "</b>")

    #print " Result : "
    print string