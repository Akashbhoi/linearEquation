# views.py
from django.shortcuts import render
from .forms import EquationForm


def home(request):
    form = EquationForm()

    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            equation1 = form.cleaned_data['equation1']
            equation2 = form.cleaned_data['equation2']
            return render(request, 'home.html',
                          {'form': form, 'equation1': equation1, 'equation2': equation2})

    return render(request, 'home.html', {'form': form})
