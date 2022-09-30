# -*- coding: utf-8 -*-
"""Li_Zachary_Fall21_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x4RvZECrmM_jogSgNQp-PlqTfVzI6KUe
"""

#Uploading files to Google Colab - training data and test data
from google.colab import files
uploaded = files.upload()

#reading uploaded file
import pandas as pd
import io
data = pd.read_csv(io.BytesIO(uploaded['stars_train.csv']))
data.head()

#extracting predictors and responses using iloc
x = data.iloc[:, [0, 3]]
y = data.iloc[:, 6]

#split into train/test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y)

#model fitting
from sklearn.tree import DecisionTreeClassifier

tree3 = DecisionTreeClassifier()
tree3.fit(x_train, y_train)

#confusion matrix plotting with test set of training data
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

predictions = tree3.predict(x_test)
cm = confusion_matrix(y_test, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

#reading final test data and extracting predictors/responses
testdata = pd.read_csv(io.BytesIO(uploaded['stars_competitor_test.csv']))
finalfeatures = testdata
finalfeatures = testdata.iloc[:, [1, 4]]

#making predictions on test data and downloading
finalpredictions = tree3.predict(finalfeatures)
df = pd.DataFrame(finalpredictions, columns = ["Predicted"])
df.to_csv('Li_Zachary_Fall21.csv')
files.download('Li_Zachary_Fall21.csv')