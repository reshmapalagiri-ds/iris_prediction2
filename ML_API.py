#import streamlit as st
import pandas as pd
import numpy as np
import pickle

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#load the dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns = iris.feature_names)
Y = iris.target
#train_test?_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
#train the model
model = RandomForestClassifier()
model.fit(x_train, y_train)
#save the model
pickle.dump(model, open('iris_model.pkl','wb'))
print("Model trained successfully ")