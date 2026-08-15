"""
Step 1 : Load the dataset
"""
import pandas as pd

df = pd.read_csv('data/train.csv')
print(df.shape)
print(df.shape)

"""
Step 2 : Select Features
"""
print(df.columns)

#Counts the number of missing values (NaN) in each column.
print(df.isna().sum())

# This line removes rows with missing Embarked values and keeps only four columns
df = df.loc[df.Embarked.notna(), ['Survived', 'Pclass', 'Sex', 'Embarked']]
print(df.shape)

print(df.isna().sum())
print(df.head())

"""
Step 3 : Cross validate a model with one feature
"""
# loc is Pandas' way of saying "select data by labels."
X = df.loc[:, ['Pclass']]
y = df.Survived

print(X.shape)
print(y.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

logreg = LogisticRegression()
print(cross_val_score(logreg, X, y, cv=5, scoring='accuracy').mean())
# Shows the proportion (percentage as a decimal) of each class in y.
# normalize=True makes value_counts() return proportions instead of raw counts.
print(y.value_counts(normalize=True))

"""
Step 4 : Encode categorical features
"""
# dummy encoding of categorical features
# Encoding = converting categorical/text data into numbers so a machine-learning model can use it.
# OneHotEncoder = creates a separate 0/1 column for each category.
# sparse=False tells OneHotEncoder to return a regular NumPy array instead of a sparse matrix.
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)

#fit() → learns the categories in Sex (female, male).
# transform() → converts those categories into one-hot encoded 0/1 columns.
print(ohe.fit_transform(df[['Sex']]))

print(ohe.categories_)

print(ohe.fit_transform(df[['Embarked']]))

print(ohe.categories_)

"""
Step 5 : Cross validate a pipeline with all features
"""
# Removes the Survived column from df.
X = df.drop('Survived', axis = 'columns')
print(X.head())

# use when different features need different preprocessing
from sklearn.compose import make_column_transformer

# Creates a column transformer that:
# OneHotEncoder() → one-hot encodes Sex and Embarked.
# remainder='passthrough' → keeps all other columns unchanged.
column_trans = make_column_transformer(
    (OneHotEncoder(), ['Sex', 'Embarked']),
    remainder='passthrough'
)

# [Sex_female, Sex_male, Embarked_C, Embarked_Q, Embarked_S, Pclass]
print(column_trans.fit_transform(X))

# Chain sequential steps together
from sklearn.pipeline import make_pipeline
# X
#  ↓
# column_trans   → encode categorical features
#  ↓
# logreg         → train/predict using the transformed data
pipe = make_pipeline(column_trans, logreg)

# cross-validate the entire process
# thus preprocessing occurs within each fold of cross validation
print(cross_val_score(pipe, X, y, cv=5, scoring='accuracy').mean())

"""
Step 6 : make predictions on new data
"""
X_new = X.sample(5, random_state=99)
print(X_new)

# X, y
#  ↓
# column_trans.fit_transform(X)
#  ↓
# logreg.fit(transformed_X, y)
pipe.fit(X, y)

print(pipe.predict(X_new))






















