'''
Given a data file with scraped data from yelp, convert it to svmlight / libsvm format
http://scikit-learn.org/stable/datasets/index.html#datasets-in-svmlight-libsvm-format

'''
from os import listdir
from os.path import isfile,join
import pickle
import collections

def make_feature_dicts():
    features = {}
    dates = {}
    closed_rest = {}
    open_rest = {}
    labels = {}

    #load feature dictionary
    with open('feature_dictionary.txt', 'r') as f:
        features = pickle.load(f)

    #load dates dictionary for closed restuarants
    with open('training_dates_dictionary.txt', 'r') as f1:
        closed_rest = pickle.load(f1)

    #load open restuarants
    with open('test_dates_dictionary.txt', 'r') as f2:
        open_rest = pickle.load(f2)

    dates = closed_rest.copy()
    dates.update(open_rest)

    return features, dates, open_rest, closed_rest

#path_to_filename is full path to file
def convert_to_svm(path_to_filename):
    unlabelled_features, dates, open_rest, closed_rest = make_feature_dicts()

    #make label dictionary
    features = collections.OrderedDict(sorted(unlabelled_features.items()))
    features['smoking']['outdoorarea/patioonly'] = 4 #this reviewer is a asshat

    reverse_labels = {}
    labels = {}
    i = 0
    for k,v in features.iteritems():
        reverse_labels[i] = k
        labels[k] = i
        i += 1

    #pickle the label files
    with open('reverse_feature_labels.txt', 'wb') as f:
        pickle.dump(reverse_labels, f)

    with open('labels_features.txt', 'wb') as f:
        pickle.dump(labels, f)

    currline = 0
    lineRet = ""

    path = path_to_filename.split('/')
    filename = path[-1][:-4]

    #change this, right now only doing 2 and 3 years
    if filename in dates:
        if filename in open_rest and open_rest[filename] < 3.0: #don't add an open restuarant unless it's been open from longer than 3 years
            lineRet += str(2) + ' '
        else:
            return ''
    else:
        print filename + " has no duration calulated yet"
        lineRet += "-1 "
    
    #make a feature file
    with open(path_to_filename, 'r') as f:
        fileDict = {}
        #make dictionary with features found in file
        for line in f.readlines():
            #handle cuisine types
            if "$" in line:
                fileDict['pricerangeperperson'] = line.strip()
            #skip date line
            elif '20' in line:
                continue
            elif ":" not in line:
                tempL = line.replace(" ","").strip().lower().split(',')
                #add each cuisine type as seperate dictionary entry
                for subline in tempL:
                    if len(subline) < 1:
                        continue
                    elif subline not in fileDict:
                        fileDict[subline] = 'yes'
            #handle other features
            else:
                tempL = line.replace(" ","").strip().lower().split(':')
                if tempL[0] not in fileDict:
                    #check if multiple attributes in feature
                    if ',' in tempL[1]:
                        fileDict[tempL[0]] = tempL[1].split(',')
                    else:
                        fileDict[tempL[0]] = tempL[1]
            currline = currline + 1
        #compare features library to features found in file
        #print fileDict
        for feature,v in features.iteritems():
            if feature in fileDict:
                if not isinstance(fileDict[feature],basestring):
                    s = 0
                    for item in fileDict[feature]:
                        #print feature, item
                        s = s + int(v[item])
                else:
                    s = int(v[fileDict[feature]])
                lineRet += str(labels[feature]) + ":" + str(s) + " "
            else:
                lineRet += str(labels[feature]) + ":0 "
    return lineRet

#convert_to_svm('data/training/javans-goleta.txt')

#convert all files, create the training set 
def make_svm():
    training_sites = listdir('data/training/')
    testing_sites = listdir('data/test/')
    svm_lines = []
    svm_names = []

    for site in testing_sites:
        temp = convert_to_svm('data/test/' + site)
        if temp is '':
            continue
        else:
            svm_lines.append(temp)
            svm_names.append(site)

    with open('test_svm_data.txt', 'wb') as f:
        for line in svm_lines:
            f.write(line + '\n')
    with open('test_rest_names.txt', 'wb') as f:
        for name in svm_names:
            f.write(name + '\n')

make_svm()




