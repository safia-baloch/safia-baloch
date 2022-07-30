# -*- coding: utf-8 -*-
"""Filter+wrapper FS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ITPWf1m_PblGSz9UgkGItxEGRHqWTVGk
"""

import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LinearRegression

#Reference: https://colab.research.google.com/notebooks/io.ipynb#scrollTo=u22w3BFiOveAå
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/ONLINE EDUCATION SYSTEM REVIEW.csv')

# #When done, 
# drive.flush_and_unmount()
# print('All changes made in this colab session should now be visible in Drive.')

from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from matplotlib import pyplot
from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

df

#df=df.drop(["Unnamed: 9","COD_S11","Cod_SPro"], axis = 1)
col=df.select_dtypes(['object']).columns
df[col]=df[col].apply(lambda x: pd.factorize(x)[0])
Dfd=df.drop(['Your level of satisfaction in Online Education'], axis=1)
Dfl=df['Your level of satisfaction in Online Education']
X=Dfd
Y=Dfl

"""**Hybrid**"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)
dfx = pd.DataFrame(data=X,columns=df.columns[1:])
from sklearn.decomposition import PCA
pca = PCA(n_components=None)
dfx_pca = pca.fit(dfx)
plt.figure(figsize=(10,6))
plt.scatter(x=[i+1 for i in range(len(dfx_pca.explained_variance_ratio_))],
            y=dfx_pca.explained_variance_ratio_,
           s=100, alpha=0.75,c='orange',edgecolor='k')
plt.grid(True)
plt.title("Explained variance ratio of the \nfitted principal component vector\n",fontsize=25)
plt.xlabel("Principal components",fontsize=15)
plt.xticks([i+1 for i in range(len(dfx_pca.explained_variance_ratio_))],fontsize=10)
plt.yticks(fontsize=15)
plt.ylabel("Explained variance ratio",fontsize=15)
plt.show()

dfx_trans = pca.transform(dfx)
dfx_trans = pd.DataFrame(data=dfx_trans)
plt.figure(figsize=(10,6))
plt.scatter(dfx_trans[0],dfx_trans[1],c=df['Your level of satisfaction in Online Education'],edgecolors='k',alpha=0.75,s=100)
plt.grid(True)
plt.title("Class separation using first two principal components\n",fontsize=10)
plt.xlabel("Principal component-1",fontsize=15)
plt.ylabel("Principal component-2",fontsize=15)
plt.show()

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, Y).transform(X)
import matplotlib.pyplot as plt

# plot size
plt.figure(figsize=(15, 8))

# plotting the graph
plt.scatter(X_r2[:,0],X_r2[:,1],  c=Y)
plt.show()

pca.explained_variance_ratio_
from sklearn.model_selection import train_test_split

# splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)
lda_model = LinearDiscriminantAnalysis(n_components=2)

# training the model
lda_model.fit(X_train, y_train)
y_pred = lda_model.predict(X_test)
from sklearn.metrics import accuracy_score

# printing the accuracy
print(accuracy_score(y_test, y_pred))

pca.explained_variance_ratio_
from sklearn.model_selection import train_test_split

# splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
pca = PCA(n_components=2)
lda_model = pca.fit(X).transform(X)

# training the model
lda_model.fit(X_train, y_train)
y_pred = lda_model.predict(X_test)
from sklearn.metrics import accuracy_score

# printing the accuracy
print(accuracy_score(y_test, y_pred))

for i in range(1,22):
  rfe_selector = SequentialFeatureSelector(estimator=LinearRegression(), n_features_to_select=i,direction='forward')
  rfe_selector.fit(X, Y.values.ravel())
  rfe_support = rfe_selector.get_support()
  rfe_feature = X.loc[:,rfe_support].columns.tolist()
  print(str(len(rfe_feature)), 'selected features',rfe_feature)
  fs=df[rfe_feature]
  fs.sample(1)
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)
  model = LogisticRegression(solver='sag', max_iter=10000)
  model.fit(X_train, y_train)
  sk_report = classification_report(
        digits=6,
        y_true=y_test, 
        y_pred=model.predict(X_test))
  print(sk_report)

for i in range(1,22):
  rfe_selector = SequentialFeatureSelector(estimator=LinearRegression(), n_features_to_select=i,direction='backward')
  rfe_selector.fit(X, Y.values.ravel())
  rfe_support = rfe_selector.get_support()
  rfe_feature = X.loc[:,rfe_support].columns.tolist()
  print(str(len(rfe_feature)), 'selected 3 features',rfe_feature)
  fs=df[rfe_feature]
  fs.sample(1)
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)
  model = LogisticRegression(solver='sag', max_iter=10000)
  model.fit(X_train, y_train)
  sk_report = classification_report(
        digits=6,
        y_true=y_test, 
        y_pred=model.predict(X_test))
  print(sk_report)

X_train, X_test, y_train, y_test = train_test_split(X, Y)
model = LogisticRegression(solver='sag', max_iter=10000)
model.fit(X_train, y_train)
sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_test))
print(sk_report)

"""**Recursive Feature Engineering: LogisticRegression:**"""

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
for i in range(1,22):
  rfe_selector = RFE(estimator=LogisticRegression(solver='sag', max_iter=10000), n_features_to_select=i, verbose=0)
  rfe_selector.fit(X, Y.values.ravel())
  rfe_support = rfe_selector.get_support()
  rfe_feature = X.loc[:,rfe_support].columns.tolist()
  print(str(len(rfe_feature)), 'selected 3 features',rfe_feature)
  fs=df[rfe_feature]
  fs.sample(1)
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)
  model = LogisticRegression(solver='sag', max_iter=10000)
  model.fit(X_train, y_train)
  sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_test))
  print(sk_report)

"""**Three Features**"""

from sklearn.feature_selection import RFE

from sklearn.tree import DecisionTreeClassifier
for i in 5,10:
  rfe_selector = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=i, verbose=0)
  rfe_selector.fit(X, Y.values.ravel())
  rfe_support = rfe_selector.get_support()
  rfe_feature = X.loc[:,rfe_support].columns.tolist()
  print(str(len(rfe_feature)), 'selected features are:  ', rfe_feature)
  fs=df[rfe_feature]
  print("With LR Model")
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)
  model = LogisticRegression(solver='sag', max_iter=10000)
 # model= DecisionTreeClassifier()
  model.fit(X_train, y_train)
  sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_test))
  print(sk_report)
  
  print("With DT Model")
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)
  model = DecisionTreeClassifier()
  model.fit(X_train, y_train)
  sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_test))
  print(sk_report)

"""**Recursive Feature Engineering: DecisionTreeClassifier: 3,5,7 Features**

Recursive
"""

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier
for i in 5,10:
  rfe_selector = RFE(estimator=RandomForestClassifier(), n_features_to_select=i, step=10,verbose=0)
  rfe_selector.fit(X, Y.values.ravel())
  rfe_support = rfe_selector.get_support()
  rfe_feature = X.loc[:,rfe_support].columns.tolist()
  print(str(len(rfe_feature)), 'selected features are:  ', rfe_feature)
  fs=df[rfe_feature]
  print("With P Model")
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)
  print("with LR Model")
  
  model = LogisticRegression(solver='sag', max_iter=10000)
  model.fit(X_train, y_train)
  sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_test))
  print(sk_report)
  print("with RF Model")
  
  model = RandomForestClassifier()
  model.fit(X_train, y_train)

  sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_test))
  print(sk_report)

print("feature importance of RF:",model.feature_importances_)

from sklearn.feature_selection import RFE

for i in 5,10:
  rfe_selector = RFE(estimator=GradientBoostingClassifier(), n_features_to_select=i, verbose=0)
  rfe_selector.fit(X, Y.values.ravel())
  rfe_support = rfe_selector.get_support()
  rfe_feature = X.loc[:,rfe_support].columns.tolist()
  print(str(len(rfe_feature)), 'selected features are:  ', rfe_feature)
  fs=df[rfe_feature]
  print("With GBC Model")
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)  
  model = GradientBoostingClassifier()
  model.fit(X_train, y_train)
  sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_test))
  print(sk_report)

#Importing the necessary packages and libaries
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
#linear = svm.SVC(kernel='linear', C=1, decision_function_shape='ovo').fit(X_train, y_train)
for i in range(1,22):
  rfe_selector = RFE(estimator=svm.SVC(kernel='linear', C=1, decision_function_shape='ovo'), n_features_to_select=i, verbose=0)
  rfe_selector.fit(X, Y.values.ravel())
  rfe_support = rfe_selector.get_support()
  rfe_feature = X.loc[:,rfe_support].columns.tolist()
  print(str(len(rfe_feature)), 'selected features with linear kernel :  ', rfe_feature)
  fs=df[rfe_feature]
  print("With SVM Model")
  X_train, X_test, y_train, y_test = train_test_split(fs, Y)
  for i in 'linear','rbf','poly','sigmoid':
    if i=='poly':
      model = svm.SVC(kernel=i,degree=3, C=1, decision_function_shape='ovo')
      model.fit(X_train, y_train)
      sk_report = classification_report(
        digits=6,
        y_true=y_test, 
        y_pred=model.predict(X_test))
      print(sk_report)
    else:
      model = svm.SVC(kernel=i, gamma=1, C=1, decision_function_shape='ovo')
      model.fit(X_train, y_train)
      sk_report = classification_report(
          digits=6,
          y_true=y_test, 
          y_pred=model.predict(X_test))
      print(sk_report)

"""**Correlation Based Feature Selection**"""

import numpy as np
import scipy.spatial as ss
from scipy.special import digamma
from math import log
import numpy.random as nr
import numpy as np
import random


# continuous estimators

def entropy(x, k=3, base=2):
    """
    The classic K-L k-nearest neighbor continuous entropy estimator x should be a list of vectors,
    e.g. x = [[1.3],[3.7],[5.1],[2.4]] if x is a one-dimensional scalar and we have four samples
    """

    assert k <= len(x)-1, "Set k smaller than num. samples - 1"
    d = len(x[0])
    N = len(x)
    intens = 1e-10  # small noise to break degeneracy, see doc.
    x = [list(p + intens * nr.rand(len(x[0]))) for p in x]
    tree = ss.cKDTree(x)
    nn = [tree.query(point, k+1, p=float('inf'))[0][k] for point in x]
    const = digamma(N)-digamma(k) + d*log(2)
    return (const + d*np.mean(map(log, nn)))/log(base)


def mi(x, y, k=3, base=2):
    """
    Mutual information of x and y; x, y should be a list of vectors, e.g. x = [[1.3],[3.7],[5.1],[2.4]]
    if x is a one-dimensional scalar and we have four samples
    """

    assert len(x) == len(y), "Lists should have same length"
    assert k <= len(x) - 1, "Set k smaller than num. samples - 1"
    intens = 1e-10  # small noise to break degeneracy, see doc.
    x = [list(p + intens * nr.rand(len(x[0]))) for p in x]
    y = [list(p + intens * nr.rand(len(y[0]))) for p in y]
    points = zip2(x, y)
    # Find nearest neighbors in joint space, p=inf means max-norm
    tree = ss.cKDTree(points)
    dvec = [tree.query(point, k+1, p=float('inf'))[0][k] for point in points]
    a, b, c, d = avgdigamma(x, dvec), avgdigamma(y, dvec), digamma(k), digamma(len(x))
    return (-a-b+c+d)/log(base)


def cmi(x, y, z, k=3, base=2):
    """
    Mutual information of x and y, conditioned on z; x, y, z should be a list of vectors, e.g. x = [[1.3],[3.7],[5.1],[2.4]]
    if x is a one-dimensional scalar and we have four samples
    """

    assert len(x) == len(y), "Lists should have same length"
    assert k <= len(x) - 1, "Set k smaller than num. samples - 1"
    intens = 1e-10  # small noise to break degeneracy, see doc.
    x = [list(p + intens * nr.rand(len(x[0]))) for p in x]
    y = [list(p + intens * nr.rand(len(y[0]))) for p in y]
    z = [list(p + intens * nr.rand(len(z[0]))) for p in z]
    points = zip2(x, y, z)
    # Find nearest neighbors in joint space, p=inf means max-norm
    tree = ss.cKDTree(points)
    dvec = [tree.query(point, k+1, p=float('inf'))[0][k] for point in points]
    a, b, c, d = avgdigamma(zip2(x, z), dvec), avgdigamma(zip2(y, z), dvec), avgdigamma(z, dvec), digamma(k)
    return (-a-b+c+d)/log(base)


def kldiv(x, xp, k=3, base=2):
    """
    KL Divergence between p and q for x~p(x), xp~q(x); x, xp should be a list of vectors, e.g. x = [[1.3],[3.7],[5.1],[2.4]]
    if x is a one-dimensional scalar and we have four samples
    """

    assert k <= len(x) - 1, "Set k smaller than num. samples - 1"
    assert k <= len(xp) - 1, "Set k smaller than num. samples - 1"
    assert len(x[0]) == len(xp[0]), "Two distributions must have same dim."
    d = len(x[0])
    n = len(x)
    m = len(xp)
    const = log(m) - log(n-1)
    tree = ss.cKDTree(x)
    treep = ss.cKDTree(xp)
    nn = [tree.query(point, k+1, p=float('inf'))[0][k] for point in x]
    nnp = [treep.query(point, k, p=float('inf'))[0][k-1] for point in x]
    return (const + d*np.mean(map(log, nnp))-d*np.mean(map(log, nn)))/log(base)


# Discrete estimators
def entropyd(sx, base=2):
    """
    Discrete entropy estimator given a list of samples which can be any hashable object
    """

    return entropyfromprobs(hist(sx), base=base)


def midd(x, y):
    """
    Discrete mutual information estimator given a list of samples which can be any hashable object
    """

    return -entropyd(list(zip(x, y)))+entropyd(x)+entropyd(y)


def cmidd(x, y, z):
    """
    Discrete mutual information estimator given a list of samples which can be any hashable object
    """

    return entropyd(list(zip(y, z)))+entropyd(list(zip(x, z)))-entropyd(list(zip(x, y, z)))-entropyd(z)


def hist(sx):
    # Histogram from list of samples
    d = dict()
    for s in sx:
        d[s] = d.get(s, 0) + 1
    return map(lambda z: float(z)/len(sx), d.values())


def entropyfromprobs(probs, base=2):
    # Turn a normalized list of probabilities of discrete outcomes into entropy (base 2)
    return -sum(map(elog, probs))/log(base)


def elog(x):
    # for entropy, 0 log 0 = 0. but we get an error for putting log 0
    if x <= 0. or x >= 1.:
        return 0
    else:
        return x*log(x)


# Mixed estimators
def micd(x, y, k=3, base=2, warning=True):
    """ If x is continuous and y is discrete, compute mutual information
    """

    overallentropy = entropy(x, k, base)
    n = len(y)
    word_dict = dict()
    for sample in y:
        word_dict[sample] = word_dict.get(sample, 0) + 1./n
    yvals = list(set(word_dict.keys()))

    mi = overallentropy
    for yval in yvals:
        xgiveny = [x[i] for i in range(n) if y[i] == yval]
        if k <= len(xgiveny) - 1:
            mi -= word_dict[yval]*entropy(xgiveny, k, base)
        else:
            if warning:
                print("Warning, after conditioning, on y={0} insufficient data. Assuming maximal entropy in this case.".format(yval))
            mi -= word_dict[yval]*overallentropy
    return mi  # units already applied


# Utility functions
def vectorize(scalarlist):
    """
    Turn a list of scalars into a list of one-d vectors
    """

    return [(x,) for x in scalarlist]


def shuffle_test(measure, x, y, z=False, ns=200, ci=0.95, **kwargs):
    """
    Shuffle test
    Repeatedly shuffle the x-values and then estimate measure(x,y,[z]).
    Returns the mean and conf. interval ('ci=0.95' default) over 'ns' runs, 'measure' could me mi,cmi,
    e.g. Keyword arguments can be passed. Mutual information and CMI should have a mean near zero.
    """

    xp = x[:]   # A copy that we can shuffle
    outputs = []
    for i in range(ns):
        random.shuffle(xp)
        if z:
            outputs.append(measure(xp, y, z, **kwargs))
        else:
            outputs.append(measure(xp, y, **kwargs))
    outputs.sort()
    return np.mean(outputs), (outputs[int((1.-ci)/2*ns)], outputs[int((1.+ci)/2*ns)])


# Internal functions
def avgdigamma(points, dvec):
    # This part finds number of neighbors in some radius in the marginal space
    # returns expectation value of <psi(nx)>
    N = len(points)
    tree = ss.cKDTree(points)
    avg = 0.
    for i in range(N):
        dist = dvec[i]
        # subtlety, we don't include the boundary point,
        # but we are implicitly adding 1 to kraskov def bc center point is included
        num_points = len(tree.query_ball_point(points[i], dist-1e-15, p=float('inf')))
        avg += digamma(num_points)/N
    return avg


def zip2(*args):
    # zip2(x,y) takes the lists of vectors and makes it a list of vectors in a joint space
    # E.g. zip2([[1],[2],[3]],[[4],[5],[6]]) = [[1,4],[2,5],[3,6]]
    return [sum(sublist, []) for sublist in zip(*args)]
def information_gain(f1, f2):
    """
    This function calculates the information gain, where ig(f1,f2) = H(f1) - H(f1|f2)
    Input
    -----
    f1: {numpy array}, shape (n_samples,)
    f2: {numpy array}, shape (n_samples,)
    Output
    ------
    ig: {float}
    """

    ig = entropyd(f1) - conditional_entropy(f1, f2)
    return ig


def conditional_entropy(f1, f2):
    """
    This function calculates the conditional entropy, where ce = H(f1) - I(f1;f2)
    Input
    -----
    f1: {numpy array}, shape (n_samples,)
    f2: {numpy array}, shape (n_samples,)
    Output
    ------
    ce: {float}
        ce is conditional entropy of f1 and f2
    """

    ce = entropyd(f1) - midd(f1, f2)
    return ce


def su_calculation(f1, f2):
    """
   
 This function calculates the symmetrical uncertainty, where su(f1,f2) = 2*IG(f1,f2)/(H(f1)+H(f2))
    Input
    -----
    f1: {numpy array}, shape (n_samples,)
    f2: {numpy array}, shape (n_samples,)
    Output
    ------
    su: {float}
        su is the symmetrical uncertainty of f1 and f2
    """

    # calculate information gain of f1 and f2, t1 = ig(f1,f2)
    t1 = information_gain(f1, f2)
    # calculate entropy of f1, t2 = H(f1)
    t2 = entropyd(f1)
    # calculate entropy of f2, t3 = H(f2)
    t3 = entropyd(f2)
    # su(f1,f2) = 2*t1/(t2+t3)
    su = 2.0*t1/(t2+t3)

    return su


def merit_calculation(X, y):
    """
    This function calculates the merit of X given class labels y, where
    merits = (k * rcf)/sqrt(k+k*(k-1)*rff)
    rcf = (1/k)*sum(su(fi,y)) for all fi in X
    rff = (1/(k*(k-1)))*sum(su(fi,fj)) for all fi and fj in X
    Input
    ----------
    X: {numpy array}, shape (n_samples, n_features)
        input data
    y: {numpy array}, shape (n_samples,)
        input class labels
    Output
    ----------
    merits: {float}
        merit of a feature subset X
    """

    n_samples, n_features = X.shape
    rff = 0
    rcf = 0
    for i in range(n_features):
        fi = X[:, i]
        rcf += su_calculation(fi, y)
        for j in range(n_features):
            if j > i:
                fj = X[:, j]
                rff += su_calculation(fi, fj)
    rff *= 2
    merits = rcf / np.sqrt(n_features + rff)
    return merits


def cfs(X, y):
    """
    This function uses a correlation based heuristic to evaluate the worth of features which is called CFS
    Input
    -----
    X: {numpy array}, shape (n_samples, n_features)
        input data
    y: {numpy array}, shape (n_samples,)
        input class labels
    Output
    ------
    F: {numpy array}
        index of selected features
    Reference
    ---------
    Zhao, Zheng et al. "Advancing Feature Selection Research - ASU Feature Selection Repository" 2010.
    """

    n_samples, n_features = X.shape
    F = []
    # M stores the merit values
    M = []
    while True:
        merit = -100000000000
        idx = -1
        for i in range(n_features):
            if i not in F:
                F.append(i)
                # calculate the merit of current selected features
                t = merit_calculation(X[:, F], y)
                if t > merit:
                    merit = t
                    idx = i
                F.pop()
        F.append(idx)
        M.append(merit)
        if len(M) > 5:
            if M[len(M)-1] <= M[len(M)-2]:
                if M[len(M)-2] <= M[len(M)-3]:
                    if M[len(M)-3] <= M[len(M)-4]:
                        if M[len(M)-4] <= M[len(M)-5]:
                            break
    return np.array(F)

def CFS_FS(X,y):
    
    '''
    This function performs a forward search for CFS
    Inputs:
    X - training data
    y - labels
    
    Outputs:
    merit_score_sel - The merit value assigned to the selected feature subsets in the order they were added
    sel_comb - The selected feature combination
    '''

    # initialise variables
    var_no = 1
    sel_comb = []
    merit_score_change = 1
    merit_score_prev = 0
    merit_score_sel = pd.DataFrame()
    enum = 0

    m,n = X.shape

    for  i in range(0,n-1):
    
        # Create a consecutive list with all the variables
        var_list = list(range(0,n))
        combs = []
        j = 0
        
        # Find the unique  combinations of variables
        if(var_no ==1):
            combs = var_list
        elif (var_no == 2):
            var_list.remove(sel_comb)
            for i in var_list:
                combs.insert(j, tuple([sel_comb,i]))
                j=j+1
        else:
            for i in sel_comb:
                var_list.remove(i)
            for i in var_list:
                combs.insert(j, sel_comb + (i,)) 
                j=j+1
            
        # Iterate through the possible feature subsets and find merit scores
        merit_score = []
        for i in range(0,len(combs)):
            X_input = X[:,combs[i]]
            if (var_no == 1):
                X_input = np.atleast_2d(X_input).T
            MS = merit_calculation(X_input, y)
            merit_score.append(MS)

        # Calculate the change in the merit score, once the score stops improving, stop the search
        merit_score_change = max(merit_score) - merit_score_prev
        if(merit_score_change <= 0):
            break
        else:
            sel_comb = combs[np.argmax(merit_score)]
            merit_score_prev = max(merit_score)
            var_no = var_no + 1

            merit_score_sel.insert(enum, enum,[ merit_score_prev])
            enum = enum+1
        
    return merit_score_sel, sel_comb

"""# New Section"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
X_tr_raw, X_ts_raw, y_train, y_test = train_test_split(X, Y, 
                                                       random_state=2, test_size=1/2)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_tr_raw)
X_test = scaler.transform(X_ts_raw)
max_length = X_train.shape[0]
feat_num = X_train.shape[1]
X_train.shape, X_test.shape
kNN = KNeighborsClassifier(n_neighbors=5)
kNN = kNN.fit(X_train,y_train)
y_pred = kNN.predict(X_test)
acc = accuracy_score(y_pred,y_test)
cv_acc = cross_val_score(kNN, X_train, y_train, cv=8)

print("X_Val on training all features: {0:.3f}".format(cv_acc.mean())) 
print("Hold Out testing all features: {0:.3f}".format(acc))

merit_score_sel, sel_comb = CFS_FS(X_train, y_train)
print("Merit Score of Selected Features: " + str(merit_score_sel.values[0]))
print("Selected Feature index: " + str(sel_comb))
# Print the selected features
feature_names_sel = df.columns[np.array(sel_comb)]
feature_names_sel
X_train_CFS_FS = X_train[:,sel_comb]
X_test_CFS_FS = X_test[:,sel_comb]

kNN_CFS_FS = kNN.fit(X_train_CFS_FS,y_train)

y_pred = kNN_CFS_FS.predict(X_test_CFS_FS)

acc_CFS_FS = accuracy_score(y_pred,y_test)
cv_acc_CFS_FS = cross_val_score(kNN_CFS_FS, X_train_CFS_FS, y_train, cv=10)

print("X_Val on training selected features: {0:.3f}".format(cv_acc_CFS_FS.mean())) 
print("Hold Out testing selected features: {0:.3f}".format(acc_CFS_FS))

Sel_feat = cfs(X_train,y_train)
Sel_feat = Sel_feat[Sel_feat!=-1]
print(Sel_feat)
# Print the names of the features selected
feature_names_sel = df.columns[Sel_feat]
feature_names_sel
# Find the merit score for the search space of the selected feature subsets
merit = []
cv_acc_CFS = []
for i in range(1,len(Sel_feat)+1):
    X_train_CFS = X_train[:,Sel_feat[0:i]]
    merit.insert(i, merit_calculation(X_train_CFS, y_train))
    kNN_CFS = kNN.fit(X_train_CFS,y_train)
    cv_acc_CFS.insert(i,cross_val_score(kNN_CFS, X_train_CFS, y_train, cv=8).mean())

print(merit)
X_test_CFS = X_test[:,Sel_feat]

kNN_CFS = kNN.fit(X_train_CFS,y_train)

y_pred = kNN_CFS.predict(X_test_CFS)

acc_CFS = accuracy_score(y_pred,y_test)
cv_acc_CFS = cross_val_score(kNN_CFS, X_train_CFS, y_train, cv=10)

print("X_Val on training selected features: {0:.3f}".format(cv_acc_CFS.mean())) 
print("Hold Out testing selected features: {0:.3f}".format(acc_CFS))

f1 = plt.figure(dpi = 70)
plt.plot(feature_names_sel, merit)
plt.title("Correlation based Feature Selection")
plt.xticks(rotation=90)
plt.xlabel("Features")
plt.ylabel("Merit Score")
plt.tight_layout()

"""**Filters**"""

import pandas as pd
import numpy as np
from sklearn.feature_selection import chi2, mutual_info_classif
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt 
X_tr_raw, X_ts_raw, y_train, y_test = train_test_split(X, Y, 
                                                       random_state=1, test_size=1/2)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_tr_raw)
X_test = scaler.transform(X_ts_raw)

feature_names = df.columns
X_train.shape, X_test.shape
#feature score with Chi Square
chi2_score, pval = chi2(X_train, y_train)
chi2_score = np.nan_to_num(chi2_score)
print("chi  square score:",chi2_score)
#feature score with Information Gain
i_scores = mutual_info_classif(X_train,y_train)
print("I-gain  score:",i_scores)
from scipy import stats
stats.spearmanr(chi2_score, i_scores)

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model = model.fit(X_train,y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_pred,y_test)
print(acc)
n_features = X_train.shape[1]
n_features
filters = [mutual_info_classif, chi2]
k_options = [n_features, 3, 5,7]
filt_scores = {}
chi_scores = {}
i_gain_scores = {}

for the_filter in filters:
    accs = []
    for k_val in k_options:
        FS_trans = SelectKBest(the_filter, 
                           k=k_val).fit(X_train, y_train)
        X_tR_new = FS_trans.transform(X_train)
        X_tS_new = FS_trans.transform(X_test)

        model.fit(X_tR_new, y_train)

        y_tS_pred = model.predict(X_tS_new)
        
        acc = accuracy_score(y_test, y_tS_pred)
        accs.append(acc)
        print(the_filter, k_val, acc)
    filt_scores[the_filter.__name__] = accs

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt 
import numpy as np
# %matplotlib inline 

fig, ax = plt.subplots()
width = 0.3
sb = 'skyblue'

options = ['All'] + k_options[1:]
ig = filt_scores['mutual_info_classif']
ch = filt_scores['chi2']

y_pos = np.arange(len(options))

p1 = ax.bar(y_pos-width, ig, width, align='center', 
            color=['red', 'blue', 'blue','blue','blue'],alpha=0.5)
p2 = ax.bar(y_pos, ch, width, align='center', 
            color=['red', sb, sb, sb, sb],alpha=0.5)

ax.legend((p1[1], p2[1]), ('I-Gain', 'Chi Squared'),loc='upper right')
ax.set_ylim([0.5, 1])
plt.grid(axis = 'y')
plt.yticks(np.arange(0.5,1.05,0.1))

plt.xticks(y_pos, options)
plt.ylabel('Test Set Accuracy')
plt.xlabel('Feature Counts')
plt.show()

cv_acc_scores = []
tst_acc_scores = []
best_acc = 0
best_k = 0
for kk in range(1, X_train.shape[1]+1):
    FS_trans = SelectKBest(mutual_info_classif, 
                           k=kk).fit(X_train, y_train)
    X_tR_new = FS_trans.transform(X_train)
    X_tS_new = FS_trans.transform(X_test)
    cv_acc = cross_val_score(model, X_tR_new, y_train, cv=10)
    cv_acc_scores.append(cv_acc.mean())
    y_pred_temp = model.fit(X_tR_new, y_train).predict(X_tS_new)
    tst_acc_scores.append(accuracy_score(y_pred_temp, y_test))
    if cv_acc.mean() > best_acc:
        best_acc = cv_acc.mean()
        best_k = kk
d=pd.DataFrame()
d['Training Acc.'] = cv_acc_scores
d['Test Acc.'] = tst_acc_scores

print(best_k, best_acc)
d.head(15)
model = LogisticRegression(solver='sag', max_iter=10000)
model.fit(X_tR_new, y_train)
sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_tS_new))
print(sk_report)

cv_acc_scores = []
tst_acc_scores = []
best_acc = 0
best_k = 0
for kk in range(1, X_train.shape[1]+1):
    FS_trans = SelectKBest(chi2, 
                           k=kk).fit(X_train, y_train)
    X_tR_new = FS_trans.transform(X_train)
    X_tS_new = FS_trans.transform(X_test)
    cv_acc = cross_val_score(model, X_tR_new, y_train, cv=8)
    cv_acc_scores.append(cv_acc.mean())
    y_pred_temp = model.fit(X_tR_new, y_train).predict(X_tS_new)
    tst_acc_scores.append(accuracy_score(y_pred_temp, y_test))
    if cv_acc.mean() > best_acc:
        best_acc = cv_acc.mean()
        best_k = kk
d=pd.DataFrame()
d['Training Acc.'] = cv_acc_scores
d['Test Acc.'] = tst_acc_scores

print(best_k, best_acc)
d.head(15)
model = LogisticRegression(solver='sag', max_iter=10000)
model.fit(X_tR_new, y_train)
sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_tS_new))
print(sk_report)

"""**Feature Selection using ReliefF**"""

pip install skrebate

from skrebate import ReliefF
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 
X_tr_raw, X_ts_raw, y_train, y_test = train_test_split(X, Y, 
                                                       random_state=42, test_size=0.3)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_tr_raw)
X_test = scaler.transform(X_ts_raw)

feature_names = df.columns
X_train.shape, X_test.shape
reliefFS = ReliefF(n_features_to_select=11, n_neighbors=50, n_jobs = -1)
reliefFS.fit(X_train,y_train.values.ravel())
relief_scores = reliefFS.feature_importances_
reliefFS.transform(X_train).shape

model = LogisticRegression(solver='sag', max_iter=10000)
model.fit(X_tR_new, y_train)
sk_report = classification_report(
      digits=6,
      y_true=y_test, 
      y_pred=model.predict(X_tS_new))
print(sk_report)
from scipy import stats
stats.spearmanr(relief_scores, i_scores)

model = LogisticRegression(solver='sag', max_iter=10000)
X_tr_relief = reliefFS.transform(X_train)
X_ts_relief = reliefFS.transform(X_test)
X_tr_relief.shape
LR_relief = model.fit(X_tr_relief,y_train)
y_pred = LR_relief.predict(X_ts_relief)
acc_11 = accuracy_score(y_pred,y_test)
acc_11