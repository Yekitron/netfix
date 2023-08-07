from django import forms

class SearchMovie(forms.Form):
    search_term = forms.CharField(label='Search movie here...', max_length=100)