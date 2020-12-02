from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader, context


# Create your views here.
from some_app.forms import SomeForm
from some_app.models import Student


def index(request):
    comm = request.GET.get('comm')
    vowels = 0
    consonants = 0
    letters = 0
    for letter in comm:
        if letter in ['a', 'o', 'i', 'u', 'e']:
            vowels += 1
        else:
            consonants += 1
        letters += 1
    return HttpResponse(f"vowels = {vowels}, consonants = {consonants}, letters = {letters}")


def get_information(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    age = request.GET.get('age')
    comment = request.GET.get('comment')
    print(f'{first_name}/{last_name}/{age}/{comment}')
    return HttpResponse(request)


def add_page(request):
    if request.method == 'GET':
        some_context = {
            'name': 'Andrey'
        }
        return render(request, 'add.html', context=some_context)


def home_page(request):
    new_list = []
    if request.method == 'GET':
        query_set = Student.objects.all()
        for student in query_set:
            new_list.append(f'{student}')
        some_context = {'students': f'Студенты: {new_list}'}
        return render(request, 'home_page.html', context=some_context)


def add(request):
    if request.method == 'GET':
        some_context_2 = {'form': Student()}
        return render(request, 'home_page.html', some_context_2)
    elif request.method == 'POST':
        form = SomeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            age = data.get('age')
            Student.objects.create(first_name=first_name, last_name=last_name, age=age)
            return redirect('/home_page/')
