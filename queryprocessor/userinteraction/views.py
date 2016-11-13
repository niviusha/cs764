from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UserQuery


def get_query_form(request):
    # When the form is generated for the first time, it has a GET request
    return render(request, 'userinteraction/user_query_input.html', {
        'form': UserQuery(request.GET)
    })

def get_results(request):
    # Checking if the form is correct and then proceeding
    if request.method == 'POST':
        form = UserQuery(request.POST)
        if form.is_valid():
            return render(request, 'userinteraction/result.html', {
                'query': form.cleaned_data['query']
            })
    else:
        form = UserQuery(request.GET)
    return render(request, 'userinteraction/user_query_input.html', {
        'form': form
    })
