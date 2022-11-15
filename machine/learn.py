import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def predict(age, sex):
    if sex == "male":
        s = 1
    elif sex == "female":
        s = 0
    else:
        return "no sex defined"

    path = '/home/ctp/Desktop/tessaract/machine/music.csv'

    music_data = pd.read_csv(path)
    # print(music_data)
    x = music_data.drop(columns = ['genre'])
    y = music_data['genre']

    model = DecisionTreeClassifier()
    model.fit(x,y)

    predictions = model.predict([[age,s]])

    return str(predictions[0])

age = 21
sex = "male"
prediction = predict(21, "male")

print(f"{age} year {sex} likes {prediction}")