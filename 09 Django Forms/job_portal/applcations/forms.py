from django import forms

from .models import JobApplication

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={"placeholder":"Your Name", "class":"form-control"})
    )

    email = forms.EmailField(
        max_length=100,
        widget = forms.EmailInput(attrs={"placeholder":"Your Email", "class":"form-control"})
    )

    message = forms.CharField(
        max_length=100,
        widget = forms.Textarea(attrs={"placeholder":"Your Placeholder", "class":"form-control", 'rows':4})
    )
    
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["name", 'email', 'phone', 'resume', 'cover_letter', "job_title"]

        widget= {
            'name': forms.TextInput(attrs={'class': 'form-control', 'pleaceholder':"Enter Full Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'pleaceholder':"Enter Email"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'pleaceholder':"Enter Phone Number"}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'pleaceholder':"Write a cover letter", 'rows':5}),
            'job_title': forms.Select(attrs={'class': 'form-control', })


        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) < 10:
            raise forms.ValidationError("Enter a valid Phone number.")
        return phone


    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if resume.size > 2 * 1024 * 1024:
                raise forms.ValidationError("File size should not exceed 2MB.")
            if not resume.name.endswith(('.pdf', '.doc', '.docx')):
                raise forms.ValidationError("Only PDF and Word documents are allowed.")
        return resume