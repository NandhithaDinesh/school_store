import re

from django import forms
from django.forms import inlineformset_factory

from .models import FormEntry, Material, Department, Course


class FormEntryForm(forms.ModelForm):
    class Meta:
        model = FormEntry
        fields = '__all__'
    dob=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
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

    # department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department')
    # course = forms.ModelChoiceField(queryset=Course.objects.none(), label='Course')

    # def __init__(self, *args, **kwargs):
    #     super( FormEntryForm, self).__init__(*args, **kwargs)
    #     self.fields['course'].queryset = Course.objects.none()
    # def __init__(self, *args, **kwargs):
    #     super(FormEntryForm, self).__init__(*args, **kwargs)
    #     self.fields['course'].queryset = Course.objects.none()
    #
    #     # Check if 'department' is in the form data and update course choices
    #     if 'department' in self.data:
    #         try:
    #             department_id = int(self.data.get('department'))
    #             self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
    #         except (ValueError, TypeError):
    #             pass  # Handle the case where 'department' is not a valid integer
