"""
Part 1 : Model building in scikit-learn (refresher)
"""

from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

print(X.shape)
print(y.shape)

"""
Features are also known as predictors, inputs or attributes
The response is also known as the target, label, or output
Observations are also known as samples, instances, or records
"""

# examine the first 5 rows of the feature matrix
import pandas as pd
df = pd.DataFrame(X, columns=iris.feature_names)
print(df.head())
print(y)

"""
In order to build a model, the features must be numeric, and every observation must have the same features in the same order
"""
# import the class
from sklearn.neighbors import KNeighborsClassifier

# instantiate the model
knn = KNeighborsClassifier()

# fit the model with data
knn.fit(X, y)

"""
In order to make a prediction, the new observation must have the same features as the training observations, both in number and meaning
"""

# predict the response for a new observation
print(knn.predict([[3, 5, 4, 2]]))

"""
Part 2 : Representing text as numeric data
"""

# example text for model training (SMS messages)
simple_train = ['call you tonight', 'Call me a cab', 'please call me... PLEASE!']

"""
From the scikit-learn documentation:
    Text Analysis is a major application field for machine learning algorithms. However the raw data, a sequence of symbols cannot be fed directly to the algorithms themselves as most of them expect numerical feature vectors with a fixed size rather than the raw text documents with variable length.
We will use CountVectorizer to "convert text into a matrix of token counts
"""

# import and instantiate CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
#Creates a text vectorizer that converts text into numerical features based on word counts.
vect = CountVectorizer()

# learn the 'vocabulary' of the training data
vect.fit(simple_train)

# Examine the fitted vocabulary
# Prints the list of words (features) that CountVectorizer learned from the text
print(vect.get_feature_names_out())

# transform training data into a 'document_term matrix'
# Converts the text in simple_train into a document-term matrix (DTM) using the vocabulary that vect already learned.
simple_train_dtm = vect.transform(simple_train)
print(simple_train_dtm)

"""
Dense matrix
    Stores every value, including zeros
Sparse matrix
    Stores only the non-zero values and their positions
"""
# Convert sparse matrix to a dense matrix
print(simple_train_dtm.toarray())

# examine the vocabulary and document-term matrix together
exam = pd.DataFrame(simple_train_dtm.toarray(), columns=vect.get_feature_names_out())
print(exam)

"""
From the scikit-learn documentation:

    In this scheme, features and samples are defined as follows:

    Each individual token occurrence frequency (normalized or not) is treated as a feature.
    The vector of all the token frequencies for a given document is considered a multivariate sample.
    A corpus of documents can thus be represented by a matrix with one row per document and one column per token (e.g. word) occurring in the corpus.

    We call vectorization the general process of turning a collection of text documents into numerical feature vectors. This specific strategy (tokenization, counting and normalization) is called the Bag of Words or "Bag of n-grams" representation. Documents are described by word occurrences while completely ignoring the relative position information of the words in the document.
"""
# Check the type of the document_term matrix
print(type(simple_train_dtm))
# examine the sparse matrix contents
print(simple_train_dtm)

"""
From the scikit-learn documentation:

    As most documents will typically use a very small subset of the words used in the corpus, the resulting matrix will have many feature values that are zeros (typically more than 99% of them).

    For instance, a collection of 10,000 short text documents (such as emails) will use a vocabulary with a size in the order of 100,000 unique words in total while each document will use 100 to 1000 unique words individually.

    In order to be able to store such a matrix in memory but also to speed up operations, implementations will typically use a sparse representation such as the implementations available in the scipy.sparse package.
"""


"""
In order to make a prediction, the new observation must have the same features as the training observations, both in number and meaning.
"""
# ecample text for model testing
simple_test = ["please don't call me"]
# transform testing data into a doncument-term matrix
simple_test_dtm = vect.transform(simple_test)
print(simple_test_dtm.toarray())

# examine the vocabulary and document_term matrix together
print(pd.DataFrame(simple_test_dtm.toarray(), columns= vect.get_feature_names_out()))

"""
Summary:

    - vect.fit(train) learns the vocabulary of the training data
    - vect.transform(train) uses the fitted vocabulary to build a document-term matrix from the training data
    - vect.transform(test) uses the fitted vocabulary to build a document-term matrix from the testing data (and ignores tokens it hasn't seen before)
"""

"""
Part 3 : Reading a text-based dataset into pandas
"""

# read file into pandas using a relative path
path = 'data//sms.tsv' 
sms = pd.read_table(path, header=None, names=['label', 'message'])


# alternative: read file into pandas from a URL
# url = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
# sms = pd.read_table(url, header=None, names=['label', 'message'])

# examine the shape
print(sms.shape)

# examine the first 10 rows
print(sms.head(10))

# examine the class distribution
print(sms.label.value_counts())

# convert label to a numerical variable
sms['label_num'] = sms.label.map({'ham':0, 'spam':1})

# check that the conversion worked
print(sms.head(10))

# how to define X and y from iris data for uses with a model
X = iris.data
y = iris.target

print(X.shape)
print(y.shape)

# how to define X and y (from the sms data) for use with countvector
X = sms.message
y = sms.label_num

print(X.shape)
print(y.shape)

# split X and y into training and testing sets


# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


"""
Part 4 : Vectorizing our dataset
"""
# instantiate the vectorizer
vect = CountVectorizer()

# learn training data vocabulary, then use it to create a document-term matrix 
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)

# equivalently: combine fit and transform into a single step
X_train_dtm = vect.fit_transform(X_train)
print(X_train_dtm)

# trabsform testing data (using fitted vocab)
print("-----------------------------------------")
X_test_dtm = vect.transform(X_test)
print(X_test_dtm)

"""
Part 5 : Building and evaluating a model
"""
"""
We will use multinomial Naive Bayes:

    The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification). The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as tf-idf may also work
"""

# import and instantiate a Multinomial Nave Bayes model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

# train the model using X_train_dtm and time it
import time
start = time.time()
nb.fit(X_train_dtm, y_train)
end = time.time()
print("Training time:", end - start, "seconds")

# make class predictions for X_test_dtm
y_pred_class = nb.predict(X_test_dtm)

# calculate accuracy of class predictions
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_class))

# print the confusion matrix
confusion = metrics.confusion_matrix(y_test, y_pred_class)
print(confusion)

# print message text for the false positives (ham incorrectly classified as spam)
FP = confusion[0][1]
print(f"{FP} false positives")
print(X_test[(y_pred_class==1)&(y_test==0)])


# print message text for the false negatives (spam incorrectly classified as ham)
FN = confusion[1][0]
print(f"{FN} false negatives")
print(X_test[(y_pred_class==0)&(y_test==1)])

# calculate predicted probabilities for X_test_dtm (poorly calibrated)
# [:, 1] means:
# : → take all rows
# 1 → take column 1, i.e. the probability of class 1
# y_pred_prob contains the probability that each message is spam.
y_pred_prob = nb.predict_proba(X_test_dtm)[:,1]
print(y_pred_prob)


# calculate AUC
print(metrics.roc_auc_score(y_test, y_pred_prob))

"""
Part 6 : Comparing models
"""
"""
We will compare multinomial Naive Bayes with logistic regression:
    Logistic regression, despite its name, is a linear model for classification rather than regression. Logistic regression is also known in the literature as logit regression, maximum-entropy classification (MaxEnt) or the log-linear classifier. In this model, the probabilities describing the possible outcomes of a single trial are modeled using a logistic function.
"""
# import and instantiate a logistic regression model
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

# train the model using X_train_dtm
start = time.time()
logreg.fit(X_train_dtm, y_train)
end = time.time()
print("Training time:", end - start, "seconds")

# make class predictions for X_test_dtm
y_pred_class = logreg.predict(X_test_dtm)

# calculate predicted probabilities for X_test_dtm (well calibrated)
y_pred_prob = logreg.predict_proba(X_test_dtm)[:, 1]
print(y_pred_prob)

# calculate accuracy
print(metrics.accuracy_score(y_test, y_pred_class))

# calculate AUC
print(metrics.roc_auc_score(y_test, y_pred_prob))

"""
Part 7 : Examining a model for further insight
    We will examine the our trained Naive Bayes model to calculate the approximate "spamminess" of each token
"""

# store the vocabulary of X_train
X_train_tokens = vect.get_feature_names_out()
print(len(X_train_tokens))

# examine the first 50 tokens
print(X_train_tokens[0:50])

# examine the last 50 tokens
print(X_train_tokens[-50:])

# Naive Bayes counts the number of times each token appears in each class
print(nb.feature_count_)

# rows represent classes, columns represent tokens
print(nb.feature_count_.shape)

# number of times each token appears across all HAM messages
ham_token_count = nb.feature_count_[0, :]
print(ham_token_count)

# number of times each token appears across all SPAM messages
spam_token_count = nb.feature_count_[1, :]
print(spam_token_count)

# create a dataframe of tokens with their separate ham and spam counts
tokens = pd.DataFrame({'token': X_train_tokens, 'ham': ham_token_count, 'spam': spam_token_count}).set_index('token')

# examine 5 randome dataframe rows
print(tokens.sample(5, random_state=6))

# naive bayes counts the number of observations in each class
print(nb.class_count_)

"""
Before we can calculate the "spamminess" of each token, we need to avoid dividing by zero and account for the class imbalance.
"""

# add 1 to ham and spam counts to aboid dividing by 0
tokens['ham'] = tokens.ham + 1
tokens['spam'] = tokens.spam + 1
print(tokens.sample(5, random_state=6))

# convert the ham and spam counts into frequencies
tokens['ham'] = tokens.ham / nb.class_count_[0]
tokens['spam'] = tokens.spam / nb.class_count_[1]
print(tokens.sample(5, random_state=6))

# calculate the ratio of spam to ham for each token
tokens['spam/ham'] = tokens.spam / tokens.ham
print(tokens.sample(5, random_state=6))

# examine the dataframe sorted by spam/ham(spam ratio)
print(tokens.sort_values('spam/ham', ascending=False))

# look up the spam_ratio for a given token
# Give me the value associated with the word "dating" in the "spam/ham" column.
print(tokens.loc['dating', 'spam/ham'])

"""
Part 8 : Practicing this workflow on another dataset
    open exercise.py
"""



"""
Part 9: Tuning the vectorizer (discussion)
"""







