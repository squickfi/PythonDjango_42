from django import forms


class RemovalForm(forms.Form):
    film_to_remove = forms.ChoiceField(choices=(), required=True)

    def __init__(self, choices, *args, **kwargs):
        super(RemovalForm, self).__init__(*args, **kwargs)
        self.fields['film_to_remove'].choices = choices
