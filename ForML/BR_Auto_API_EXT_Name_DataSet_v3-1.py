from warnings import catch_warnings

import pefile
import pandas as pd
import os
import sys
import numpy as np

path_category = r'C:\Users\br179\Capstone\category_test'
Category_List = os.listdir(path_category)

for category_name in Category_List:
    print(category_name)
    ## file_list
    path_name = r'C:\Users\br179\Capstone\category_test' + '\\' + category_name + '\exe_name'
    file_name = os.listdir(path_name)
    file_name = [file for file in file_name if file.endswith(".exe")]  # exe파일 이름만 도출하기위한 코드

    #' ' 뺀 file_list
    file_list=[]
    for i in file_name:
        file_list.append(i[:-4])
    file_list


    # 프로그램별 api_list (API_List.csv)
    api_list = pd.read_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_List.csv")
    api_list = api_list.drop(api_list.columns[0:1], axis='columns')

    # 중복제거된 모든 api_name (API_Name.csv)
    api_name = pd.read_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_Name.csv")
    api_name = api_name.drop(api_name.columns[0:1], axis='columns')

    # api_list to type of list , 전체 api (column),
    # ex)GetProcAddress', 'GetModuleHandleA', 'LoadLibraryA',...
    # api name -> list
    api_name_column = api_name.values.tolist()
    api_name_column = np.ravel(api_name_column, order='C')

    # api_name_dataset
    data_set = pd.DataFrame(index=file_list, columns=api_name_column)
    # dataset에 값 채워 넣기
    for i in file_list:
        f1 = api_list.loc[:,[i]].dropna()
        arr = f1.values.tolist()
        arr = np.ravel(arr,order='C')
        for j in api_name_column:
            if(j in arr):
                data_set.loc[i,j] = 1
            else:
                data_set.loc[i,j] = 0

    # api별 각 api를 사용한 프로그램수 추가
    for i in api_name_column:
        data_set.loc['Used_Program_count',i]= int(data_set.loc[:,[i]].sum())

    data_set.to_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_Name_DataSet.csv")

    # 여기까지 프로그램수 찾기 위한 코드
    # 아래부터 임계치 이상의 api에 대한 dataset 생성

    # 임계치 이상의 api를 list에 추가

    # 임계치 7.5%
    new_api=[]
    for i in api_name_column:
        if(data_set.loc['Used_Program_count',i]>=5): # 임계치 = 5
            new_api.append(i)

    file = open("C:\\Users\\br179\\api\\" + category_name + "\\apiList_75.txt", 'w')

    for i in new_api:
        file.write(i+"\n")
    file.close()

    # 임계치 10%
    new_api2=[]
    for i in api_name_column:
        if(data_set.loc['Used_Program_count',i]>=6): # 임계치 = 6
            new_api2.append(i)

    file2 = open("C:\\Users\\br179\\api\\" + category_name + "\\apiList_10.txt", 'w')

    for i in new_api2:
        file2.write(i + "\n")
    file2.close()

###################################################################################################
total_api_name=[]
api_list=[]
for category_name in Category_List:
    api_list = open("C:\\Users\\br179\\api\\"+ category_name + "\\apiList_75.txt", 'r').read().split('\n')
    del api_list[-1]
    total_api_name += api_list

a= pd.DataFrame()
for category_name in Category_List:

    file_list
    path_name = r'C:\Users\br179\Capstone\category_test' + '\\' + category_name + '\exe_name'
    file_name = os.listdir(path_name)
    file_name = [file for file in file_name if file.endswith(".exe")]  # exe파일 이름만 도출하기위한 코드

    # ' ' 뺀 file_list
    file_list = []
    for i in file_name:
        file_list.append(i[:-4])
    file_list

    # 프로그램별 api_list (API_List.csv)
    api_list = pd.read_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_List.csv")
    api_list = api_list.drop(api_list.columns[0:1], axis='columns')

    real_data_set = pd.DataFrame(index=file_list, columns=total_api_name)

    for i in file_list:
        f1 = api_list.loc[:,[i]].dropna()
        arr = f1.values.tolist()
        arr = np.ravel(arr,order='C')
        for j in total_api_name:
            if(j in arr):
                real_data_set.loc[i,j] = 1
            else:
                real_data_set.loc[i,j] = 0
    real_data_set["Category"] = category_name
    a = pd.concat([a, real_data_set])

a.to_csv("C:\\Users\\br179\\api\\API_Name_DataSet_cv75.csv")

print("----------")
print(" complete ")
print("----------")



