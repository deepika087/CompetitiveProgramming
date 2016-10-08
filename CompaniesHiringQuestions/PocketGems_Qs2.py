"""
This is qs2
Qs1 was to do BFS/DFS

Objective:

Write a program that will read a log file and calculate the percent of time a player had network connectivity.

Details:

We have several games that involve connecting to our servers via the network. Mobile network conditions can be very different between devices, providers, and so on. For diagnostic reasons it's important to know what portion of the time a given player spends actually connected to the network.

We keep console logs of various game subsystems for each play session. Each log message has the following format:

(MM/dd/yyyy-hh:mm:ss) :: [message logged]

Sample log lines:

(11/12/2015-02:34:56) :: START
(01/02/1990-13:10:00) :: DISCONNECTED
(03/13/2018-21:01:01) :: ERROR - File "close.png" not found.
Log messages that pertain to network connectivity are as follows:

START : Logged when the game starts up.
CONNECTED : Logged when a network connection is established.
DISCONNECTED : Logged when network connection is lost.
SHUTDOWN : Logged when the player is quitting the game.
A player's session length is the amount of time between the START and SHUTDOWN messages.
A player's connected time is the amount of time they spend in a connected state. A player starts the game disconnected, becomes connected when we log aCONNECTED message, and becomes disconnected when we log a DISCONNECTED message.

You can make the following assumptions:

All logs will be properly formatted
All dates will be valid
No log message will stretch across multiple lines
All log files will be ordered chronologically
There will always be exactly one START and exactly one SHUTDOWN event logged
Input

A file containing lines of log messages.

Output

The connectivity percentage as a string, rounded down to an integer.

Examples

(01/01/2000-01:00:00) :: START
(01/01/2000-01:01:00) :: CONNECTED
(01/01/2000-01:21:00) :: DISCONNECTED
(01/01/2000-01:50:00) :: SHUTDOWN
The player spent 20 minutes out of 50 connected, 20 / 50 = 0.4, output should be "40%"
(02/03/2002-14:00:00) :: START
(02/03/2002-14:00:00) :: CONNECTED
(02/03/2002-14:08:00) :: DISCONNECTED
(02/03/2002-14:10:00) :: CONNECTED
(02/03/2002-14:15:00) :: SHUTDOWN
The player spent 13 minutes out of 15 connected, 13 / 15 = 0.8667, output should be "86%"
More sample input can be found in the text files input_1.txt, input_2.txt, and input_3.txt

To compile your code on the command line, use this command:
g++ -std=c++0x -o LogParser LogParser.cpp -DUSE_MAIN
To run the generated executable file, use this command:
./LogParser

Your answer must be able to be compiled with g++ using the c++0x standard.
"""
from datetime import datetime, date, time

def getDateTime(currDate, currTime):
    currDate = currDate.split('/')
    currTime = currTime.split(':')
    d = date(int(currDate[2]), int(currDate[1]), int(currDate[0])) #YEar, month, date
    t = time(int(currTime[0]), int(currTime[1]), int(currTime[2]))
    dt = datetime.combine(d, t)
    return dt

def getDifference(dt2, dt1):
    return (dt2-dt1).seconds/60

if __name__ == "__main__":
    lines = [line.rstrip('\r\n') for line in open('/Users/deepika/PycharmProjects/PythonPrograms/CompaniesHiringQuestions/input.txt')]

    startDate = None
    startTime = None
    endDate = None
    endTime = None
    connectedTime = 0 #Total duration the programmr was connected
    seenConnected = False
    connDate = None
    connTime = None
    runningTime = 0

    for line in lines:
        line = line.replace('(', '').replace(')', '')
        items = line.split("::")
        #print items
        if (items[1] == " START"):
            startDate = (items[0].split('-'))[0]
            startTime = (items[0].split('-'))[1]
        elif (items[1] == ' SHUTDOWN'):
            endDate = (items[0].split('-'))[0]
            endTime = (items[0].split('-'))[1]
            dt2 = getDateTime(endDate, endTime)
            dt1 = getDateTime(startDate, startTime)
            runningTime = runningTime + getDifference(dt2, dt1)

        if (items[1] == " CONNECTED"):
            seenConnected = True
            connDate = (items[0].split('-'))[0]
            connTime = (items[0].split('-'))[1]

        elif ( items[1] in [" DISCONNECTED", " SHUTDOWN"] and seenConnected == True):
            currDate = (items[0].split('-'))[0]
            currTime = (items[0].split('-'))[1]
            dt2 = getDateTime(currDate, currTime)
            dt1 = getDateTime(connDate, connTime)
            minutes_diff = getDifference(dt2, dt1)
            connectedTime = connectedTime + minutes_diff
            seenConnected = False

    print str(int((float(connectedTime/float(runningTime)) * 100))) + "%"