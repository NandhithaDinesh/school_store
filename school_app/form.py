import re

from django import forms
from .models import FormEntry, Material


class FormEntryForm(forms.ModelForm):
    class Meta:
        model = FormEntry
        fields = '__all__'

    name = forms.CharField(max_length=100,required=True,error_messages={'required':'Req',})
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
    )
    materials_provided = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')

        # Add your validation logic here
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long.')

        return name

    phone_number = forms.CharField(max_length=15, required=True)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        # Define a regular expression for a valid phone number
        phone_number_pattern = re.compile(r'^\+?1?\d{9,15}$')

        if not phone_number_pattern.match(phone_number):
            raise forms.ValidationError('Enter a valid phone number.')

        return phone_number