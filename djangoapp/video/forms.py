from django import forms

class searchForm(forms.Form):
    search_keyword = forms.CharField(max_length=100)

