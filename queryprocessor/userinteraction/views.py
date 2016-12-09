from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from forms import UserQuery, ReformQuery


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
                'query': form.cleaned_data['query'],
                'form': ReformQuery(request.GET)
            })
    else:
        form = UserQuery(request.GET)
    return redirect("/user_query_input")

def train_system(request):
  if request.method == 'POST':
    form = ReformQuery(request.POST)
    if form.is_valid():
      correct_query = form.cleaned_data['query']
  return redirect("/user_query_input")
