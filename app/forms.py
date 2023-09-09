from django import forms

def check_for_s(value):
    if value[0]=='s':
        raise forms.ValidationError('Name starts wit s')
    
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('name length is less than 5 characters')
    
class Studentform(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_s,check_for_len])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[check_for_s])