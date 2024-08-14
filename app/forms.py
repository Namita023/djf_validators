from typing import Any
from django import forms

#normal functions
def check_for_len(value):
    if len(value)<3:
        raise forms.ValidationError('Length is too short')

def check_for_z(value):
    if value[0].lower()=='z':
        raise forms.ValidationError("Name shouldn't start with z")

class StudentForm(forms.Form):
    student_id=forms.IntegerField()
    student_name=forms.CharField(max_length=100,validators=[check_for_len,check_for_z])
    student_age=forms.IntegerField()
    student_email=forms.EmailField()
    rmail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    
    #form class object method: clean
    def clean(self):
        em=self.cleaned_data['student_email']
        rem=self.cleaned_data['rmail']
        sa=self.cleaned_data['student_age']
        if rem!=em or sa<18:
            raise forms.ValidationError('Error')
        
    #form class object method: clean_element
    # def clean_student_age(self):
    #     sage=self.cleaned_data['student_age']
    #     if sage<18:
    #         raise forms.ValidationError('Underage')
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>=0:
            raise forms.ValidationError('bot')