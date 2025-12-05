from django.shortcuts import render,redirect

# Create your views here.
from app.models import student_model
from app.forms import student_form

def details(request):
    data = student_model.objects.all()
    return render(request,'table.html',{'data':data})

def post_data(request):
    form = student_form()
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mydata')
    else:
        form = student_form()
    return render(request,'form.html',{'form':form})