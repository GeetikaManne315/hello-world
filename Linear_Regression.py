import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

class MyLinearRegression:   # changed class name
    def __init__(self):      # fix constructor
        self.data = None

    def LoadData(self, file_path):
        self.data = pd.read_csv(file_path)
        return self.data
    
    def NumericData(self, columns):
        if self.data is None:
            print("No data Loaded. Check the file path.")
        self.data[columns] = self.data[columns].fillna(self.data[columns].mean())
        return self.data
    
    def StandardizeData(self, columns):
        if self.data is None:
            print("No data Loaded. Check the file path.")
        
        for column in columns:
            mean = self.data[column].mean()
            std = self.data[column].std()
            self.data[column] = (self.data[column] - mean) / std
        return self.data
    
    def EncodeCategorical(self, columns):
        model = OneHotEncoder()
        encoded_data = model.fit_transform(self.data[columns])
        self.data = self.data.drop(columns, axis=1)
        self.data = pd.concat(
            [self.data, pd.DataFrame(encoded_data.toarray(), 
             columns=model.get_feature_names_out(columns))],
            axis=1)
        return self.data
    
    def SplitData(self, target_column, test_size=0.2):
        X = self.data.drop(target_column, axis=1)
        y = self.data[target_column]
        return train_test_split(X, y, test_size=test_size)
    
    def TrainModel(self, X_train, y_train):
        model = LinearRegression()   # sklearn model
        model.fit(X_train, y_train)
        return model
    
    def EvaluateModel(self, model, X_test, y_test):
        return model.score(X_test, y_test)
    
    def Predict(self, model, new_data):
        return model.predict(new_data)

def main():
    lr = MyLinearRegression()
    data = lr.LoadData(r"C:\Users\geetu\Desktop\hello world\bookstore_inventory.csv")
    print(data.head())
    list1 = data.select_dtypes(include=['number']).columns.tolist()
    numeric_data = lr.NumericData(list1)
    data = pd.concat([numeric_data, data.drop(list1, axis=1)], axis=1)
    print(data.head())
    list2 = data.select_dtypes(include=['object']).columns.tolist()
    encoded_data = lr.EncodeCategorical(list2)
    data = pd.concat([encoded_data, data.drop(list2, axis=1)], axis=1)
    print(data.head())
    data.info()
    X_train, X_test, y_train, y_test = lr.SplitData(target_column='extended_retail', test_size=0.2)
    print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")
    model = lr.TrainModel(X_train, y_train)
    score = lr.EvaluateModel(model, X_test, y_test)
    print(f"Model R^2 Score: {score}")
    predictions = lr.Predict(model, X_test.iloc[:5])
    print(f"Predictions for first 5 entries in X_test: {X_test.iloc[:5]} ,{predictions}")
main()
