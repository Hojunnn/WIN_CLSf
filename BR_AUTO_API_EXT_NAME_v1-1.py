import pefile
import pandas as pd
import os
import sys

path_category = r'C:\Users\br179\Capstone\category_test'
Category_List = os.listdir(path_category)

for category_name in Category_List:

    ## 해당 카테고리 API_List 불러옴
    df = pd.read_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_List.csv")
    df = df.drop(df.columns[0:1], axis='columns')

    ## 첫번째 프로그램에 대한 api만 먼저 추출
    df_first = df.iloc[:,0:1]
    df_first.columns= ['API_Name']
    df_first= df_first.dropna()
    df_first.to_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_Name.csv")

    ## 2번째 프로그램 부터 api 추출
    for i in range(1,len(df.columns)):
        df1 = df.iloc[:,i:i+1]
        df1.columns = ['API_Name']
        df1 = df1.dropna()
        df2 = pd.read_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_Name.csv")
        df2 = df2.drop(df2.columns[0:1], axis='columns')
        df_final = pd.concat([df2,df1])
        df_final.duplicated()
        df_final = df_final.drop_duplicates()
        df_final.to_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_Name.csv")

    # 마지막으로 중복검사
    f1 = pd.read_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_Name.csv")
    f1 = f1.drop(f1.columns[0:1], axis='columns')
    f1.duplicated()
    f1=f1.drop_duplicates()
    f1.to_csv("C:\\Users\\br179\\api\\" + category_name + "\\" + category_name + "_API_Name.csv")

print("----------")
print(" complete ")
print("----------")