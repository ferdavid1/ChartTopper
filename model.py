import pandas as pd
from sklearn.cross_validation import train_test_split
from Modelrithm import Modelrithm
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

data = pd.read_csv('prediction_data.csv',sep='\s*,\s*', engine='python')
successes_raw = data['successes']
features_raw = data.drop('successes', axis = 1)
features_raw_2 = features_raw.dropna(how='any')
# print(900-681)-> 219

# One-hot encode the 'features_raw' data using pandas.get_dummies()
features = pd.get_dummies(features_raw_2)

not_successful = [s for s in successes_raw if s==1.0]
zeros = []
for zero in range(int(len(not_successful))):
	zeros.append(0)
successful = [s for s in successes_raw if s>1.0]
ones = []
for one in range(int(len(successful))):
	ones.append(1)

successes = successes_raw.replace(not_successful, zeros)
successes = successes.replace(successful, ones)
successes = successes[:-219]

# Split the 'features' and 'income' data into 70/30 training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, successes, test_size = 0.3, random_state = 0) 


'''Use Modelrithm, a Machine Learning classification algorithm framework (built by Fernando Espinosa for SBHacks 2017)
to find out which sklearn classification algorithm will output the highest accuracy, precision, and f-beta scores'''
Modelrithm.Classification(x_test, x_train, y_test, y_train)

# print(prediction)

'''The output of print(prediction) was:

-------------------------------------------------------------------

Testing your data on the following models: ['SVC()', 'KNeighborsClassifier()', 'DecisionTreeClassifier()', 'RandomForestClassifier()', 'AdaBoostClassifier()', 'GaussianNB()', 'LogisticRegression()']

-------------------------------------------------------------------

This may take a while, make yourself comfortable...

*****

The accuracy of each model is: 
{'LogisticRegression': 0.92016806722689071, 'GaussianNB': 0.91806722689075626, 'KNeighborsClassifier': 0.92016806722689071, 'RandomForestClassifier': 0.91596638655462181, 'DecisionTreeClassifier': 0.85504201680672265, 'SVC()': 0.92016806722689071, 'AdaBoostClassifier': 0.90756302521008403}

The precision of each model is: 
{'LogisticRegression': 0.92016806722689071, 'GaussianNB': 0.92000000000000004, 'KNeighborsClassifier': 0.92016806722689071, 'RandomForestClassifier': 0.91983122362869196, 'DecisionTreeClassifier': 0.91460674157303368, 'SVC()': 0.92016806722689071, 'AdaBoostClassifier': 0.92274678111587982}

The F-beta score of each model is: 
{'LogisticRegression': 0.9584245076586434, 'GaussianNB': 0.95728368017524645, 'KNeighborsClassifier': 0.9584245076586434, 'RandomForestClassifier': 0.95614035087719285, 'DecisionTreeClassifier': 0.92185730464326143, 'SVC()': 0.9584245076586434, 'AdaBoostClassifier': 0.95132743362831862}

*****



'''
clf = SVC()
clf.fit(x_train, y_train)
prediction = clf.predict(x_test)

'''The most accurate (92%) algorithms were, according to Modelrithm, LogisticRegression and SVC. SVC returned a prediction of:
[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  0.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  0.  1.  1.  1.
  1.  1.  1.  1.  1.  1.  1.]
for the test set, where a '1' indicates a song in the training set remaining on the billboard top 100 for another week, and '0' indicates it leaving the top 100'''
