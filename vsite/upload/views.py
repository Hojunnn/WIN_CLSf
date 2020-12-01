from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import os
import zipfile
import pefile
import pandas as pd
import pickle
import joblib
from xgboost import XGBClassifier
from xgboost import plot_importance

def my_view(request):
    category_name = ["Audio Player", "Video Player", "Browser", "FTP", "Game", "Image Viewer", "Network",
                     "Office",
                     "Security", "Social", "Utility"]
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    # Handle file upload
    cat=""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print("파일")
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'],name=request.POST['name'],exe_name=request.POST['exe_name'])
            print("success")
            print(str(request.FILES['docfile'])[:-4])
            zipfile.ZipFile(request.FILES['docfile']).extract(request.POST['exe_name'],'./exe/'+str(request.FILES['docfile'])[:-4])
            print("압출풀기 성공")
            my_zip = zipfile.ZipFile(request.FILES['docfile'])
            a = my_zip.namelist()
            ico=""
            for i in a:
                if (i.endswith(".ico")):
                    ico=i
                    zipfile.ZipFile(request.FILES['docfile']).extract(ico, './mainapp/static/mainapp/ico')
                    ico_path = '../../static/mainapp/ico/' + ico

            if(ico == ""):
                ico_path = '../../static/mainapp/ico/default.ico'
            print("ico:"+ico)
            print("ico_path : "+ico_path)

            path = './exe/'+str(request.FILES['docfile'])[:-4]+"/"+ str(request.POST['exe_name'])
            pe = pefile.PE(path)
            pe.parse_data_directories()
            file = open('./exe/'+str(request.FILES['docfile'])[:-4]+"\\bb.txt", "w")
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                for imp in entry.imports:
                    if str(imp.name) != 'None':
                        if '$' in str(imp.name):
                            if (str(imp.name).split('$')[0][2:] != '@'):
                                file.write(str(imp.name).split('$')[0][2:] + "\n")
                        else:
                            file.write(str(imp.name)[2:-1] + "\n")
            file.close()

            ## dataset 가져오기
            path = './exe/API_Name_DataSet_cv10.csv'
            df = pd.read_csv(path)
            df = df.drop(df.columns[0], axis='columns')

            col = df.columns

            new_api = open(r'./exe/'+str(request.FILES['docfile'])[:-4]+'/bb.txt', 'r').read().split('\n')  # 위에서 만든 실행파일 api list

            num = len(df)

            for i in col:
                df.loc[num, i] = 0

            for i in col:
                for j in new_api:
                    if (i in j):
                        df.loc[550, i] = 1

            arr = df.iloc[550:,:-1]
            rf = joblib.load('./exe/filename.pkl')
            print("load model")
            pred = rf.predict(arr)
            print("category : "+str(pred[0])+"번")

            cat = category_name[int(pred[0])]
            newdoc = Document(docfile=request.FILES['docfile'],name=request.POST['name'],exe_name=request.POST['exe_name'],category=cat,ico=ico_path)
            newdoc.save()
            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'category_name':category_name,'cat':cat}
    return render(request, 'upload/list.html', context)