import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors \
     import KNeighborsClassifier
from sklearn.model_selection \
     import train_test_split
from sklearn.inspection \
     import DecisionBoundaryDisplay
from sklearn.metrics \
     import confusion_matrix

data0 = pd.read_csv('datasetA.csv', 
                    sep=',', header=None)
data1 = pd.read_csv('datasetB.csv', 
                    sep=',', header=None)
X = pd.concat([data0, data1])
label = len(data0)*[0] + len(data1)*[1]

X_train, X_test, y_train, y_test = \
    train_test_split(X, label, 
    train_size=0.1, random_state=4)

clf = KNeighborsClassifier(n_neighbors = 3)

clf.fit(X_train, y_train)

fig, ax = plt.subplots(1,1)
cm = 'bwr_r'

DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cm, alpha=0.8, ax=ax)

predi = clf.predict(X_test)
score = clf.score(X_test, y_test)
print('Confusion matrix = ')
print(confusion_matrix(predi, y_test))
print(f'Accuracy = {score:.3}')

for i,(c1,c2) in enumerate(zip(y_test,predi)):
    if c1 != c2:
        x = X_test.iloc[i, 0]
        y = X_test.iloc[i, 1]
        print(f'({x},{y}) is classified as '
              f'{c2} but should be {c1}') 

ax.scatter(X_train.iloc[:,0],X_train.iloc[:,1], 
           c=y_train, cmap=cm, marker ='x')
ax.scatter(X_test.iloc[:,0], X_test.iloc[:,1],
           c=predi, cmap=cm, edgecolors="k",
           alpha=0.5,)

ax.set_title(r'kNN classification')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
