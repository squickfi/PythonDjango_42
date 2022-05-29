from django import forms


class UpdateForm(forms.Form):
    film_to_update = forms.ChoiceField(choices=(), required=True)
    opening_crawl = forms.CharField(required=True)

    def __init__(self, choices, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['film_to_update'].choices = choices
