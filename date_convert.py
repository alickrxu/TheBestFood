#import datetime
from datetime import date
from datetime import timedelta
import pickle
import os


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
    print name
    with open("data/test/"+name+".txt", "r") as f:
        for line in f:
            lines.append(line)
    if len(lines) == 0:
        return '1000-01-02' 
    d2 = lines[-1]
    d1 = lines[-2]
    if '20' in d2:
        temp = d2.strip().split('-')
        date2 = date(int(temp[0]),int(temp[1]),int(temp[2]))
        if '20' in d1:
            temp = d1.strip().split('-')
            date1 = date(int(temp[0]),int(temp[1]),int(temp[2]))
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

def dateConvert(closedOnly=True,closedFile='closed.txt'):
    #closedFile = 'closed.txt'
    if closedOnly:
        data = getDates(closedFile)
    else:
        data = os.listdir("./"+str(closedFile)+"/")
    dates = {}
    for place in data:
        #get the start date
        #print place
        if closedOnly:
            if place[2].strip() != '?':
                tempDate = place[2].strip().split('-')
            else:
                tempDate = getMissingDate(place[1]).split('-')
            if len(tempDate) == 2:
                start = date(int(tempDate[0]),int(tempDate[1]),1)
            else:
                start = date(int(tempDate[0]),int(tempDate[1]),int(tempDate[2]))
        else:
            tempDate = getMissingDate(place[:-4]).split('-')
            start = date(int(tempDate[0]),int(tempDate[1]),int(tempDate[2]))
        #get the close date
        if closedOnly:
            if place[3].strip() != '?':
                tempDate = place[3].strip().split('-')
            else:
                tempDate = getMissingDate(place[1],True).split('-')
            if len(tempDate) == 2:
                close = date(int(tempDate[0]),int(tempDate[1]),1)
            else:
                close = date(int(tempDate[0]),int(tempDate[1]),int(tempDate[2]))
        else:
            close = date.today()
        #calculate duration
        durationDelta = close - start
        duration = float(durationDelta.days)/365.0
        if closedOnly:
            dates[place[1]] = abs(duration)
        else:
            dates[place[:-4]] = abs(duration)
    print dates
    with open("test_dates_dictionary.txt", "w") as f:
        pickle.dump(dates,f)
    return dates

#dateConvert(False,'./soemthing/my_train_dir')
#dateConvert(True,'close_file.txt')
