from django import forms


class History(forms.Form):
    your_string = forms.CharField(label='your string')
