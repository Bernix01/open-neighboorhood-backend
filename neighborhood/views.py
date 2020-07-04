from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render, redirect
from neighborhood.models import Person
from neighborhood.forms import PersonForm


# Create your views here.
def index(request):
    persons_from_db = Person.objects.all()

    form = PersonForm()

    context_dict = {'persons_from_context': persons_from_db, 'form': form}

    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'index.html', context_dict)
