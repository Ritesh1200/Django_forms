from django.shortcuts import render
from .forms import NormalFroms , ModelForms

# Create your views here.

def NormalForm(request):
    if request.method == "GET" :
        fm = NormalFroms( label_suffix="-" )
        return render(request , "forms/normalform.html", {"form":fm})
    if request.method == "POST" :
        fm = NormalFroms(request.POST)
        if fm.is_valid():
            print("this is valid form")
            print(fm.cleaned_data["name"] , fm.cleaned_data["email"] , fm.cleaned_data["password"]  )
        else:
            print("this is not valid form")
        return render(request , "forms/normalform.html", {"form1":fm})

def ModalForm(request):
    if request.method == "GET" :
        fm = ModelForms( label_suffix="-" )
        return render(request , "forms/modelform.html", {"form":fm})
    if request.method == "POST" :
        fm = ModelForms(request.POST)
        if fm.is_valid():
            print("this is valid form")
            print(fm.cleaned_data["name"] , fm.cleaned_data["email"] , fm.cleaned_data["password"]  )
        else:
            print("this is not valid form")
        return render(request , "forms/normalform.html", {"form1":fm})
