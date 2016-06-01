'''
Get the ages for open training data.
Create open training data by getting a couple of test data and manually verifying the age

'''
from os import listdir
from os.path import isfile,join
import sys

sys.path.insert(0, '/Users/alickxu/Documents/UCSBClasses/TheBestFood')
import date_convert

mypath = 'data/test/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

converted = date_convert.dateConvert(False,'data/test/')

print converted
