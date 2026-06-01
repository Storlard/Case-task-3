from django.shortcuts import render
from .forms import NameForm
from .models import Greeting

def home(request):
    message = ""

    if request.method == "POST":
        form = NameForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            Greeting.objects.create(name=name)

            message = f"Привет, {name}!"
        else:
            message = "Ошибка: введите имя"
    else:
        form = NameForm()

    return render(request, 'greetings/home.html', {
        'form': form,
        'message': message
    })
