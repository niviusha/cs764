from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UserQuery


def get_query_form(request):
    if request.method == 'POST':
        form = UserQuery(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/result/')
    else:
        form = UserQuery(request.GET)
    return render(request, 'userinteraction/user_query_input.html', {
        'form': form
    })

def get_results(request):
    return render(request, 'userinteraction/result.html')
