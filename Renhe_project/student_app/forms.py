from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from .models import Student
from .models import School
class StudentForm(ModelForm):
    def __init__(self, data=None,*args, **kwargs):
        super(StudentForm, self).__init__(data,*args, **kwargs)

        is_scholorship=data.get('is_scholorship',None)
        print("is_scholorship:",is_scholorship)        
        

        if not is_scholorship:
            print("test")
            self.fields["scholorship_amount"].widget = HiddenInput()
    class Meta:
        model = Student
        widgets={
            'scholorship_amount':ModelForm.TextInput(attrs={'id':'scholorship_amount','disabled':True}),
        }