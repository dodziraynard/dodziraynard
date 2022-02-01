from django import forms

from .models import Article


class WalletForm(forms.ModelForm):
    description = forms.CharField(label='Description',
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Article
        fields = ["description"]
