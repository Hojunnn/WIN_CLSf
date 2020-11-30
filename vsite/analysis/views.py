import os
import pickle

import pandas as pd
from django.conf import settings
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class Train(views.APIView):
    def post(self, request):
        #request.POST. mutable = True
        path = r'C:\Users\br179\Capstone\API_Name_DataSet_cv10.csv'
        df = pd.read_csv(path)
        df = df.drop(df.columns[0], axis='columns')
        df
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 100)
        model_name = request.data.pop('model_name')
        print("Dfsdfdf")
        print(y_test)
        if model_name == 'model_1':
            try:
                #clf = KNeighborsClassifier(**request.data)
                clf = RandomForestClassifier(**request.data)
                #clf = GradientBoostingClassifier(**krequest.data)
                clf.fit(X_train, y_train)
                # accuracy = clf.score(X_train,y_train) # 학습 정확도
                accuracy = clf.score(X_test, y_test) # 테스트 정확도
                print("good")
            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
            path = os.path.join(settings.MODEL_ROOT, model_name)
            with open(path,'wb') as file:
                pickle.dump(clf,file)
            return Response("모델의 정확도 : " + str(accuracy), status=status.HTTP_200_OK)

        elif model_name == 'model_2':
            try:
                #clf = KNeighborsClassifier(**request.data)
                clf = RandomForestClassifier(**request.data)
                # clf = GradientBoostingClassifier(**request.data)
                clf.fit(X_train, y_train)
                # accuracy = clf.score(X_train,y_train) # 학습 정확도
                accuracy = clf.score(X_test, y_test)  # 테스트 정확도
            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
            path = os.path.join(settings.MODEL_ROOT, model_name)
            with open(path,'wb') as file:
                pickle.dump(clf,file)
            return Response("모델의 정확도 : " + str(accuracy), status=status.HTTP_200_OK)

class Predict(views.APIView):
    def post(self, request):
        print(self)
        predictions = []
        for entry in request.data:
            model_name = entry.pop('model_name')
            path = os.path.join(settings.MODEL_ROOT, model_name)
            with open(path, 'rb') as file:
                model = pickle.load(file)
            try:
                result = model.predict(pd.DataFrame([entry]))
                predictions.append(result[0])
                print(result[0])
            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(predictions)+"번 카테고리", status=status.HTTP_200_OK)
