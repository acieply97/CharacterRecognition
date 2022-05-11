from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from recognition.forms import DocumentForm
from ocr.engine import Engine
from recognition.models import Document


def test_view(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        Engine.start_engine(uploaded_file_url)

        return render(request, 'recognition/test.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'recognition/test.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            choice = cd['choice']
            obj = Document.objects.last()
            file = obj.document.name

            Engine.start_engine(file, choice)
            return redirect('test2')
    else:
        form = DocumentForm()
    return render(request, 'recognition/model_form_upload.html', {
        'form': form
    })


def ocr_engine_start(request):
    pass