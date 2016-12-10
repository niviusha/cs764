from sys import path
path.append("../nlp")
from final_wrapper import Wrapper
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from forms import UserQuery, ReformQuery


sentence = None
query = None

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
            global sentence, query
            sentence = form.cleaned_data['query']
            query, result = Wrapper.get_query_and_result(sentence)
            return render(request, 'userinteraction/result.html', {
                'query': query,
                'form': ReformQuery(request.GET),
                'result': result,
            })
    else:
        form = UserQuery(request.GET)
    return redirect("/user_query_input")

class ChatterBotAppView(TemplateView):
    template_name = "userinteraction/app.html"

def train_system(request):
  if request.method == 'POST':
    form = ReformQuery(request.POST)
    global sentence, query
    if form.is_valid() and form.cleaned_data['query'].strip():
      query = form.cleaned_data['query']
    Wrapper.train_sentence(sentence, query)
  return redirect("/user_query_input")

