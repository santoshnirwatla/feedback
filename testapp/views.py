from django.shortcuts import render
from testapp.forms import Student

# Create your views here.
def Student_info(request):
    form=Student()
    submitted =False
    sname = ''
   
    if request.method == 'POST':
        form = Student(request.POST)
        if form.is_valid():
            print('this is suceesfull valid')
            print('name:',form.cleaned_data['name'])
            print('Email:',form.cleaned_data['mail'])
            print('mobile num:',form.cleaned_data['mobile'])
            print('rollno:',form.cleaned_data['rollno'])
            print('feedback:',form.cleaned_data['feedback'])
            submitted = True
            sname =form.cleaned_data['name']
   
    return render(request,'testapp/index.html',{'form':form,'submitted':submitted,'name':sname})