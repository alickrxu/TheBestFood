#import datetime
from datetime import date
from datetime import timedelta


def getDates(filename):
    dates = []
    with open(filename, 'r') as f:
        for line in f:
            place = line.replace(" ","").strip().split(',')
            #print place
            dates.append(place)
    return dates

def getMissingDate(name,closeDate=False):
    #use false to get the start date, else get the close date
    lines = []
    with open("training\\"+name+".txt", "r") as f:
        for line in f:
            lines.append(line)
    d1 = lines[-1]
    d2 = lines[-2]
    if '20' in d2:
        temp = d2.strip().split('-')
        date1 = date(int(temp[0]),int(temp[1]),int(temp[2]))
        if '20' in d1:
            temp = d1.strip().split('-')
            date2 = date(int(temp[0]),int(temp[1]),int(temp[2]))
            if date1 < date2:
                if closeDate:
                    return d2
                else:
                    return d1
            else:
                if closeDate:
                    return d1
                else:
                    return d2
        else:
            return d2
    elif '20' in d1:
        return d1
    else:
        return '1000-01-01'

def dateConvert(closedFile='closed.txt'):
    #closedFile = 'closed.txt'
    data = getDates(closedFile)
    dates = {}
    for place in data:
        #get the start date
        print place
        if place[2].strip() != '?':
            tempDate = place[2].strip().split('-')
        else:
            tempDate = getMissingDate(place[1]).split('-')
        if len(tempDate) == 2:
            start = date(int(tempDate[0]),int(tempDate[1]),1)
        else:
            start = date(int(tempDate[0]),int(tempDate[1]),int(tempDate[2]))
        #get the close date
        if place[3].strip() != '?':
            tempDate = place[3].strip().split('-')
        else:
            tempDate = getMissingDate(place[1],True).split('-')
        if len(tempDate) == 2:
            close = date(int(tempDate[0]),int(tempDate[1]),1)
        else:
            close = date(int(tempDate[0]),int(tempDate[1]),int(tempDate[2]))
        #calculate duration
        durationDelta = close - start
        duration = float(durationDelta.days)/365.0
        dates[place[1]] = abs(duration)
    print dates
    return dates

#dateConvert()
