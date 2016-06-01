'''
Given restuarants in svm format with features, predict whether they will last 1,2,3 or more years

'''
from sklearn import svm, metrics, cross_validation
from sklearn.datasets import load_svmlight_file
from sklearn.feature_selection import RFECV
from sklearn.cross_validation import StratifiedKFold
import pickle
import matplotlib.pyplot as plt


#load data
X, y = load_svmlight_file("svm_data.txt")

#run cross validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.5, random_state=0)

print 'training shape before: ' + str(X_train.shape) + ', ' + str(y_train.shape)

#create classifier - svm
clf = svm.SVC(kernel='linear',C=1) #.fit(X_train, y_train)
'''
print clf.score(X_test, y_test)

#test cv score
scores = cross_validation.cross_val_score(clf, X, y, cv=5)
print scores
'''

#reduce features
rfecv = RFECV(estimator=clf, step=1, cv=8, scoring='accuracy')
rfecv.fit(X, y)

print('Optimal number of features : %d' % rfecv.n_features_)
print str(rfecv.support_)
print str(rfecv.ranking_)
print str(rfecv.grid_scores_)

num_to_name = {}

with open('reverse_feature_labels.txt', 'r') as f:
    num_to_name = pickle.load(f)

i = 0
while i < len(rfecv.ranking_):
    if rfecv.ranking_[i] == 1:
        print '1: feature ' + str(i) + ': ' + num_to_name[i]
    elif rfecv.ranking_[i] == 2:
        print '2: feature ' + str(i) + ': ' + num_to_name[i]
    elif rfecv.ranking_[i] == 3:
        print '3: feature ' + str(i) + ': ' + num_to_name[i]
    elif rfecv.ranking_[i] == 4:
        print '4: feature ' + str(i) + ': ' + num_to_name[i]
    elif rfecv.ranking_[i] == 5:
        print '5: feature ' + str(i) + ': ' + num_to_name[i]
    elif rfecv.ranking_[i] == 6:
        print '6: feature ' + str(i) + ': ' + num_to_name[i]
    elif rfecv.ranking_[i] == 7:
        print '7: feature ' + str(i) + ': ' + num_to_name[i]
    elif rfecv.ranking_[i] == 8:
        print '8: feature ' + str(i) + ': ' + num_to_name[i]
    i += 1
'''
# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()
'''

#now we do prediction

#load test data
new_X_test, new_y_test = load_svmlight_file('test_svm_data.txt')

test_results = rfecv.predict(new_X_test)

i = 0
with open('test_rest_names.txt', 'r') as f:
    for line in f.readlines():
        if test_results[i] == 2:
            print line + ' will fail in 3 years'
        else:
            print line + ' is staying alive'
        i += 1

