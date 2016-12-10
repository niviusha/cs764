from django import forms

class UserQuery(forms.Form):
    query = forms.CharField(label="Enter your query", widget=forms.Textarea, required=True)

class ReformQuery(forms.Form):
    query = forms.CharField(label="Enter the correct query that should have been evaluated", widget=forms.Textarea, required=True)
