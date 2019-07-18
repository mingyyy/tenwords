from django.shortcuts import render, redirect
from .models import Responder, User
from .forms import InputForm
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        # check if the code is related to a user
        code = request.POST['code']
        user_len = -len(code)+4
        related_user = code[user_len:]
        x = User.objects.filter(username=related_user)
        if x:
            if form.is_valid():
                form.save()
                messages.success(request, 'Thank you for your opinion!')
                return redirect('core:result')
        else:
            messages.warning(request, 'You have entered a wrong code!')

    else:
        form = InputForm()

    context = {'form': form}
    return render(request, 'core/home.html', context)


def result(request):
    results = Responder.objects.all()
    context = {'results':results}
    return render(request, 'core/result.html', context)
