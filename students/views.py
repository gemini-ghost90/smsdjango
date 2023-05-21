from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import StudentForm, ContactForm
from .models import Student, Contact

# Create your views here.


def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            }
            )
    else:
        form = StudentForm()

    return render(request, 'students/add.html', {
        'form': StudentForm()
    })


def cform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            new_f_name = form.cleaned_data['f_name']
            new_l_name = form.cleaned_data['l_name']
            new_contact_number = form.cleaned_data['contact_number']
            new_email_address = form.cleaned_data['email_address']
            new_address = form.cleaned_data['address']
            new_message = form.cleaned_data['message']

            new_contact = Contact(
                f_name=new_f_name,
                l_name=new_l_name,
                contact_number=new_contact_number,
                email_address=new_email_address,
                address=new_address,
                message=new_message
            )
            new_contact.save()
            return render(request, 'students/contactform.html', {
                'form': ContactForm(),
                'sendmail': True
            })
    else:
        form = ContactForm()

    return render(request, 'students/contactform.html', {
        'form': ContactForm()
    })


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })

    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
