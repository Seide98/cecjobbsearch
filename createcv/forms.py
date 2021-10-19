from django import forms
from .models import PostCreateCV

class CreateCVForm(forms.ModelForm):
    class Meta:
        model = PostCreateCV
        fields = ('cvname',)
        exclude = ('user',)
        widgets = {
            'cvname': forms.TextInput(attrs={'class': 'form-control'}),

        }