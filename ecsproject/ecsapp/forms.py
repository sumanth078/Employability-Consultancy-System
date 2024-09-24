from django import forms
from .models import JobSeekerRegistration, Admin, RecruiterRegistration, Contactus, RecruiterPostedJobs, \
    Seekerapplyforjob, Resume


class DateInput(forms.DateInput):
    input_type = "date"

class JobSeekerRegistrationForm(forms.ModelForm):
    class Meta:
        model = JobSeekerRegistration
        fields = "__all__"                 # it will display all the fields the forms except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput()}  # additional features of the fields

class RecruiterRegistrationForm(forms.ModelForm):
    class Meta:
        model = RecruiterRegistration
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class PostedJobsForm(forms.ModelForm):
    class Meta:
        model = RecruiterPostedJobs
        fields = "__all__"
        widgets = {"dateofbirth": DateInput()}

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class UpdateSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeekerRegistration
        fields = "__all__"

class SeekerapplyforjobForm(forms.ModelForm):
    class Meta:
        model = Seekerapplyforjob
        fields = "__all__"

class UpdateRecruiterForm(forms.ModelForm):
    class Meta:
        model = RecruiterRegistration
        fields = "__all__"

class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = "__all__"

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"
        labels = {"category":"Select Category"}