import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, roc_curve
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix, classification_report
from sklearn.pipeline import Pipeline
import numpy as np

df = pd.read_csv("./Cleaned_train_df.csv")

def predict_age(database, pred_list):
    # Should make the list into a 2D array
    the_list = [pred_list]
    # Up until the next comment, this is creating the log model
    y = database["Age>=12"]
    X = database.drop(["Age", "id", "Age>=12"], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    scaler = StandardScaler()
    scaled_X_train = scaler.fit_transform(X_train)
    scaled_X_test = scaler.transform(X_test)
    log_model = LogisticRegression()
    log_model.fit(scaled_X_train, y_train)
    # Used to get the predictions to use later in presenting the accuracy score
    y_pred = log_model.predict(scaled_X_test)
    # Creates a prediction of the information entered
    prediction = log_model.predict(the_list)
    # Displays the result
    print("Your crab is " + str(prediction) + " with an accuracy score of " + str(int(accuracy_score(y_test, y_pred)*100)) + "%")

