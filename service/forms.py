from django import forms
from .models import Issue, Volunteer

class issueform(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'name', 'contact', 'location', 'issue_type', 'description', 'issue_img'
        ]

class volunteerform(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'name', 'contact', 'location', 'availability', 'work_area'
        ]
        widgets = {
            'availability': forms.SelectDateWidget(),
        }
