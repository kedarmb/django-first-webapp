from django import forms
from testapp.models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"

        #OR
        #fields=('emp_name','emp_email','emp_address')
