from django import forms

from amexpert.models import Member


class NewMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'fullname',
            'email',
            'photo',
            'linkedin',
            'github',
            'website',
            'bio',
            'pronouns'
        ]