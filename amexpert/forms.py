from django import forms
from django_ckeditor_5.fields import CKEditor5Field


class NewMemberForm(forms.Form):
    PRONOUNS= [
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Sir', 'Sir'),
        ('Madam', 'Madam')
    ]
    fullname = forms.CharField(label='Full name', max_length=200, required=True)
    email = forms.EmailField(label='Email', required=True, max_length=200)
    linkedin = forms.URLField(label='LinkedIn', required=False)
    github = forms.URLField(label='Github', required=False)
    website = forms.URLField(label='Website', required=False)
    bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)
    pronouns = forms.ChoiceField(label='Pronouns', widget=forms.Select, choices=PRONOUNS)
