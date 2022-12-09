import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

import matplotlib.pyplot as plt
import  seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def pearson_corr(x, y):
    x['label'] = y
    xcorr = x.corr().abs()
    #setting up matplotlib
    f, ax = plt.subplots(figsize=(25,25))

    #generating mask
    mask = np.triu(np.ones_like(xcorr, dtype=bool))

    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    sns.heatmap(xcorr, annot=True, mask=mask, cmap=cmap)
    plt.savefig("Corr_Heatmap.png")

    #selecting best features
    bestfeatures = SelectKBest(k=5)
    fit=bestfeatures.fit(x, y)

    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(x.columns)

    featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    featureScores.columns = ['Specs', 'Score']

    print(featureScores)
def main():
    xTrain = pd.read_csv("xTrain.csv")
    yTrain = pd.read_csv("yTrain.csv")
    xTest = pd.read_csv("xTest.csv")
    yTest = pd.read_csv("yTest.csv")

    # #concat x and y together
    # temp = pd.concat([xTrain, yTrain], axis=1)
    #
    # #remove rows where postal codes aren't numbers (US postal codes)
    # temp = temp[temp['postal_code'].str.contains(pat = '[a-zA-Z]', regex=True) == False]
    #
    # #split back to x, y
    # xTrain = temp.drop(columns=temp.columns[-2:], axis=1)
    # yTrain = temp.iloc[:, -2:]
    #
    # #concat x and y together
    # temp = pd.concat([xTest, yTest], axis=1)
    #
    # #remove rows where postal codes aren't numbers (US postal codes)
    # temp = temp[temp['postal_code'].str.contains(pat = '[a-zA-Z]', regex=True) == False]
    #
    # #split back to x, y
    # xTest = temp.drop(columns=temp.columns[-2:], axis=1)
    # yTest = temp.iloc[:, -2:]

    #remove city and state because they're strings
    xTrain.drop(columns=['city'], inplace=True)
    #print(xTrain['state'].unique().size)

    yTrain = yTrain['starsBin']

    #remove city and state because they're strings
    xTest.drop(columns=['city'], inplace=True)

    yTest = yTest['starsBin']

    #normalize
    scaler = preprocessing.StandardScaler()
    scaler.fit(xTrain)

    xTrainNum = scaler.transform(xTrain)
    xTestNum = scaler.transform(xTest)

    # finding similarities between attributes after normalizing
    #pd.DataFrame(xTrainNum, columns=xTrain.columns)
    #pearson_corr(xTrain, yTrain)

    #model
    clf = LogisticRegression(random_state=0).fit(xTrainNum, yTrain)
    #clf = Perceptron(tol=1e-3, random_state=0).fit(xTrain, yTrain)

    yPred = clf.predict(xTestNum)

    # print('accuracy: ', accuracy_score(yTest, yPred))
    print('f1: ', f1_score(yTest, yPred))
    
if __name__ == "__main__":
    main()