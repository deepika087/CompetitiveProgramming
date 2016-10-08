
"""
Zappos coding challenge
The problem was that given coordinate of boat/plance we had to figure out
If that coordinate was inside bermuda triangle or not.
"""
def bermuda(x1, y1, x2, y2, x3, y3, px, py, bx, by):
    if ((x2 - x1)*(y3 - y1) - (y2 - y1) * (x3 - x1)) == 0:
        print "0"
    else:
        boat = False
        #check for boat
        alpha = ((y2 - y3)*(bx - x3) + (x3 - x2)*(by - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        beta = ((y3 - y1)*(bx - x3) + (x1 - x3)*(by - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        gamma = float(1.0 - alpha - beta);

        if (alpha >= 0 and beta >= 0 and gamma >= 0): # point on or inside
            boat = True

        plane = False
        #check for plane
        alpha = ((y2 - y3)*(px - x3) + (x3 - x2)* (py - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        beta = ((y3 - y1)*(px - x3) + (x1 - x3)* (py - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        gamma = float(1.0 - alpha - beta);

        if (alpha >= 0 and beta >= 0 and gamma >= 0): # point on or inside
            plane = True

        if (plane == True and boat == False):
            print "1"
        elif (plane == False and boat == True):
            print "2"
        elif (plane == True and boat == True):
            print "3"
        elif (plane == False and boat == False):
            print "4"

if __name__=="__main__":
    coordinates = raw_input('');
    coordinates =coordinates.split()

    bermuda(int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3]), int(coordinates[4]), int(coordinates[5]),
            int(coordinates[6]), int(coordinates[7]),
            int(coordinates[8]), int(coordinates[9]))