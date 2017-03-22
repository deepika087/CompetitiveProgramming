
# Complete the function below.


def pointsBelongToTriangle( x1,  y1,  x2,  y2,  x3,  y3,  p1,  q1,  p2,  q2): #(p1, q1) is boat
    if ((x2 - x1)*(y3 - y1) - (y2 - y1) * (x3 - x1)) == 0:
        return "0"

    else:
        bx=p1
        by=q1
        boat = False #Equaivalent of point P
        #check for boat
        alpha = ((y2 - y3)*(bx - x3) + (x3 - x2)*(by - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        beta = ((y3 - y1)*(bx - x3) + (x1 - x3)*(by - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        gamma = float(1.0 - alpha - beta);

        if (alpha >= 0 and beta >= 0 and gamma >= 0): # point on or inside
            boat = True

        plane = False #equ
        #check for plane
        px=p2
        py=q2
        alpha = ((y2 - y3)*(px - x3) + (x3 - x2)* (py - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        beta = ((y3 - y1)*(px - x3) + (x1 - x3)* (py - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
        gamma = float(1.0 - alpha - beta);

        if (alpha >= 0 and beta >= 0 and gamma >= 0): # point lie on or inside
            plane = True

        pointP=boat
        pointQ=plane
        if (pointP and not pointQ):
            return "1"
        elif(not pointP and pointQ):
            return "2"
        elif(pointP and pointQ):
            return "3"
        elif(not pointP and not  pointQ):
            return "4"
