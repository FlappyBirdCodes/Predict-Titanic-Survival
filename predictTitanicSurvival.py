import pandas as pd
from sklearn.linear_model import LogisticRegression

# Importing csv data
training_data = pd.read_csv("train.csv")
testing_data = pd.read_csv("test.csv")

# Adding labels to testing data
testing_labels = pd.read_csv("gender_submission.csv")
testing_data["Survived"] = testing_labels["Survived"]

# Merging csv files into one merged file
training_data = pd.concat(
    [training_data, testing_data], axis=0, ignore_index=True).to_csv("merged.csv")

training_data = pd.read_csv("merged.csv")

# Reshaping data to acceptable format
training_data.loc[training_data.Sex == "female", "Sex"] = 0
training_data.loc[training_data.Sex == "male", "Sex"] = 1
training_data = training_data.replace(
    float("nan"), training_data.Age.mean(), regex=True)

# Separating data based inputs and outputs
x = training_data[[
    "Pclass", "Sex", "Age", "Fare"]]
y = training_data[["Survived"]]

# Training logistic regression model
model = LogisticRegression()
model.fit(x, y.values.ravel())

print(model.score(x, y))
