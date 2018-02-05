from django.http import HttpResponseRedirect

from django.urls import reverse
from django.shortcuts import render

from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            c_d = form.cleaned_data
            s = Student()
            s.name = c_d['name']
            s.sex = c_d['sex']
            s.email = c_d['email']
            s.profession = c_d['profession']
            s.qq = c_d['qq']
            s.phone = c_d['phone']
            s.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)
