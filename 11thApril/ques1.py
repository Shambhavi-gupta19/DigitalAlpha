import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset= pd.read_csv("adult.csv",header=0)

#Droping missing data:

dataset=dataset.replace(" ?",np.nan)
dataset=dataset.replace(' <=50K',0)
dataset=dataset.replace(' >50K',1)
print(dataset.shape)
dataset=dataset.dropna()
print(dataset.shape)

print(list(dataset.columns))

#Visualisation:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib','inline')

pd.crosstab(dataset.Workclass,dataset.salary).plot(kind='bar')
plt.title('Workclass vs Salary')
plt.xlabel('Workclass')
plt.ylabel('Salary frequency')
plt.show()

pd.crosstab(dataset['Education num'],dataset.salary).plot(kind='bar')
plt.title('Education vs Salary')
plt.xlabel('Education Num')
plt.ylabel('Salary Frequency')
plt.show()

pd.crosstab(dataset.Occupation,dataset.salary).plot(kind='bar')
plt.title('Occupation vs Salary')
plt.xlabel('Occupation')
plt.ylabel('Salary Frequency')
plt.show()

pd.crosstab(dataset.Relationship,dataset.salary).plot(kind='bar')
plt.title('Relationship vs Salary')
plt.xlabel('Relationship')
plt.ylabel('Salary Frequency')
plt.show()

pd.crosstab(dataset.Race,dataset.salary).plot(kind='bar')
plt.title('Race vs Salary')
plt.xlabel('Race')
plt.ylabel('Salary Frequency')
plt.show()

#Dummy variables:
cat_vars=['Workclass', 'Education','Martial', 'Occupation', 'Relationship', 'Race', 'Gender',
       'Country']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(dataset[var], prefix=var)
    data=dataset.join(cat_list)
    dataset=data
cat_vars=['Workclass', 'Education','Martial', 'Occupation', 'Relationship', 'Race', 'Gender',
       'Country']
data_vars=dataset.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]

data_final=dataset[to_keep]
data_final.columns.values
data_final_vars=data_final.columns.values.tolist()
X=[i for i in data_final_vars if i not in 'salary']
print(len(X))

#RFE:
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
rfe = RFE(logreg, 15)
rfe = rfe.fit(data_final[X], data_final['salary'])
print(rfe.support_)
print(rfe.ranking_)
cols=[]
for i in range(104):
    if rfe.ranking_[i] == 1:
        cols.append(data_final_vars[i])
print(cols)    

X=data_final[cols]
y=data_final['salary'] 
print(y)
print(X)

#implementing model:
from scipy import stats
stats.chisqprob=lambda  chisq, df:stats.chi2.sf(chisq,df)
import statsmodels.api as sm

logit_model=sm.Logit(y.astype(float),X.astype(float))
result=logit_model.fit()
print(result.summary())

#Model fitting:
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

#K Fold:
from sklearn import model_selection

kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))

#Confusion Matrix:
from sklearn.metrics import confusion_matrix

confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

#Classification Report:
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

#ROC:
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()
