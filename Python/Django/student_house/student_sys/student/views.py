from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .models import Student
from .forms import StudentForm


class IndexView(View):
    template_name = 'index.html'

    def context(self):
        students = Student.objects.all()
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
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
        context = self.context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)
