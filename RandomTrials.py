
if __name__ =="__main__":

    count = 0
    for line in open('output.txt'):
        count = count + 1
        if (count == 3):
            print "This is the thrid line" , line
            count = count + 1
            break;