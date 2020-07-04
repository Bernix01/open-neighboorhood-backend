from django import forms
from neighborhood.models import Person
from open_neighborhood import settings


class PersonForm(forms.ModelForm):
    id_card = forms.CharField(max_length=20, help_text="Enter an id card")
    first_name = forms.CharField(max_length=100, help_text="Enter a first_name")
    second_name = forms.CharField(max_length=100, help_text="Enter a second_name")
    birth = forms.DateField(help_text="Enter a birth", input_formats=settings.DATE_INPUT_FORMATS)
    status = forms.BooleanField(help_text="Status")

    class Meta:
        model = Person
        fields = ('id_card', 'first_name', 'second_name', 'birth', 'status',)
