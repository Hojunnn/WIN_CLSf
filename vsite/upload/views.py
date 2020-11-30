from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print("파일")
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'],name=request.POST['name'],category=request.POST['category'])
            print(request.POST)
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
    context = {'documents': documents, 'form': form}
    return render(request, 'upload/list.html', context)