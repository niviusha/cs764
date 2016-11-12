from django import forms

class UserQuery(forms.Form):
    query = forms.CharField(label="Enter your query", widget=forms.Textarea, required=True)
