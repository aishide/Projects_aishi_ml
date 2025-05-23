from google.colab import files
uploaded = files.upload()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'])

cv = CountVectorizer()
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

model = MultinomialNB()
model.fit(X_train_cv, y_train)

X_train_array = X_train_cv.toarray()
words = cv.get_feature_names_out()
df_counts = pd.DataFrame(X_train_array, columns=words)

# Display first few rows
df_counts.head()

msg = input("Enter a message: ")
msg_cv = cv.transform([msg])
print("Spam!!!!!!!!" if model.predict(msg_cv)[0] else "Not Spam!!!")
