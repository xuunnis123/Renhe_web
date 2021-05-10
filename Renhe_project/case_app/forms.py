from django import forms
from .models import Case
from school_app.models import School
from student_app.models import Student
class CaseModelForm(forms.ModelForm):
    #school = forms.ModelChoiceField(queryset=School.objects.all())
    #name = forms.ModelChoiceField(queryset=Student.objects.all())
    class Meta:
        model = Case
        fields='__all__'
        widgets = {
            'phone' : forms.TextInput(),
            'contribute_context' : forms.TextInput(),
            'scholorship_amount' : forms.TextInput(),
            'total_money' : forms.TextInput(),
            'situation' : forms.TextInput(),
            'visited_form' : forms.TextInput(),
            'visited_photos' : forms.TextInput(),
            'start_date' : forms.TextInput(),
            'end_date' : forms.TextInput()
        }
        labels = {
             'name' : '姓名', 
            'phone' : '電話',
            'school' :'學校',
            'contribute_context' : '資助項目',
            'scholorship_amount' : '獎學金金額',
            'total_money' : '資助總金額',
            'situation' : '個案情況',
            'visited_form' : '訪視表',
            'visited_photos' : '訪視照片',
            'start_date' : '個案開始日',
            'end_date' : '個案結束日'


        }
    
class SchoolForm(forms.Form):
    school= forms.CharField(max_length=255)