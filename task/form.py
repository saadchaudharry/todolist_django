from django import forms
from .models import Tasks


class Task_form(forms.ModelForm):
    class Meta:
        model =Tasks
        fields =['complete_date','subject','detail','status']
        widgets = {'complete_date': forms.DateInput(format=('%m/%d/%Y'), attrs={ 'placeholder':'Select a date', 'type':'date'}),}
