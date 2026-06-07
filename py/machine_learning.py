# import pandas as pd
# df = pd.read_csv("vgsales.csv")
# df

# df.shape

# df.describe()

# df.values

# print("hello world")
# print("ocean")

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn import tree

music_data = pd.read_csv("music.csv")
music_data
X = music_data.drop(columns=["genre"])
X
Y = music_data["genre"]
Y
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

tree.export_graphviz(model,
                     out_file="music_recommender.dot",
                     feature_names=["age", "gender"],
                     class_names=sorted(y.unique()),
                     label="all",
                     rounded=True,
                     filled=True)

model = joblib.load("music_recommender.joblib")
joblib.dump(model, "music_recommender.joblib")

predictions = model.predict(X_test) # [[21, 1],[22, 0]]
predictions

score = accuracy_score(Y_test, predictions)
score